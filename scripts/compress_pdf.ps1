param(
  [Parameter(Mandatory=$true)]
  [string]$InputPdf,

  [ValidateSet("screen", "ebook", "printer", "prepress")]
  [string]$Quality = "ebook"
)

$inputPath = Resolve-Path $InputPdf
$dir = Split-Path $inputPath
$name = [System.IO.Path]::GetFileNameWithoutExtension($inputPath)
$output = Join-Path $dir "$name-$Quality.pdf"

$gs = Get-Command gswin64c -ErrorAction SilentlyContinue

if (-not $gs) {
  $candidates = Get-ChildItem "C:\Program Files\gs" -Recurse -Filter gswin64c.exe -ErrorAction SilentlyContinue |
    Sort-Object FullName -Descending

  if ($candidates.Count -gt 0) {
    $gsPath = $candidates[0].FullName
  } else {
    Write-Error "Ghostscript not found. Install Ghostscript first."
    exit 1
  }
} else {
  $gsPath = $gs.Source
}

Write-Host "Using Ghostscript: $gsPath"

& $gsPath -sDEVICE=pdfwrite `
  -dCompatibilityLevel=1.4 `
  -dPDFSETTINGS="/$Quality" `
  -dNOPAUSE -dQUIET -dBATCH `
  -sOutputFile="$output" `
  "$inputPath"

Write-Host "Compressed PDF created: $output"