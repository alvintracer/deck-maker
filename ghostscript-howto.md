1. 프로젝트별 레퍼런스 PDF는 projects/[project]/assets/에 둔다.
2. 공용 디자인 레퍼런스 PDF는 shared-assets/references/design/에 둔다.
3. 원본은 필요하면 Git LFS 또는 Git 제외.
4. 압축본 `*-ebook.pdf`만 일반적으로 ChatGPT/에이전트 참조용으로 사용.
5. 너무 크면 `*-screen.pdf`도 만든다.

##스크립트화 시켰을떄

MAC: ./scripts/compress_pdf.sh
projects/hana-stablecoin-proposal/assets/reference.pdf ebook

Window: powershell -ExecutionPolicy Bypass -File scripts\compress_pdf.ps1
projects\hana-stablecoin-proposal\assets\reference.pdf ebook

ebook -> screen으로 바꾸면 더 작아짐.

Mac에서 PDF 압축 명령

예를 들어:

gs -sDEVICE=pdfwrite\
-dCompatibilityLevel=1.4\
-dPDFSETTINGS=/ebook\
-dNOPAUSE -dQUIET -dBATCH\
-sOutputFile=compressed.pdf\
input.pdf

더 작게 만들고 싶으면 /ebook 대신 /screen.

gs -sDEVICE=pdfwrite\
-dCompatibilityLevel=1.4\
-dPDFSETTINGS=/screen\
-dNOPAUSE -dQUIET -dBATCH\
-sOutputFile=compressed-small.pdf\
input.pdf

품질 기준은 이렇게 보면 돼.

/screen = 가장 작음, 디자인 참고용으로 충분할 때 /ebook = 추천 기본값, 화면
확인용 품질 /printer = 더 선명함, 용량은 덜 줄어듦 /prepress = 인쇄 고품질, 용량
감소 적음

지금 deck-maker 구조 기준으로 추천

네 repo 구조가 이미 잘 잡혀 있으니까, PDF 압축은 scripts/에 하나 만들어두는 게
좋아.

추천 위치:

deck-maker/ scripts/ compress_pdf.ps1 # Windows용 compress_pdf.sh # Mac용
projects/ 각 프로젝트/ assets/ reference-original.pdf reference-ebook.pdf

운영 기준은 이렇게.

projects/[deck-name]/assets/ reference-original.pdf # 원본, 필요하면 Git 제외
또는 LFS reference-ebook.pdf # Git에 올릴 압축본 reference-screen.pdf # 더 작은
참고용

공통 디자인 레퍼런스라면:

shared-assets/ references/ design/ original/ compressed/

현재 shared-assets/가 logos, diagrams 중심이라면 아래 폴더 하나 추가하면 깔끔해.

shared-assets/references/design/ Windows용 압축 스크립트 예시

deck-maker/scripts/compress_pdf.ps1로 저장.

param( [Parameter(Mandatory=$true)]
  [string]$InputPdf,

[string]$Quality = "ebook" )

$inputPath = Resolve-Path $InputPdf $dir = Split-Path $inputPath
$name = [System.IO.Path]::GetFileNameWithoutExtension($inputPath) $output =
Join-Path $dir "$name-$Quality.pdf"

$settings = "/$Quality"

gswin64c -sDEVICE=pdfwrite `-dCompatibilityLevel=1.4` -dPDFSETTINGS=$settings `
  -dNOPAUSE -dQUIET -dBATCH `
  -sOutputFile="$output" ` "$inputPath"

Write-Host "Compressed PDF created: $output"

실행:

powershell -ExecutionPolicy Bypass -File scripts\compress_pdf.ps1
projects\hana-stablecoin-proposal\assets\reference.pdf ebook

또는 더 작게:

powershell -ExecutionPolicy Bypass -File scripts\compress_pdf.ps1
projects\hana-stablecoin-proposal\assets\reference.pdf screen Mac용 압축
스크립트 예시

deck-maker/scripts/compress_pdf.sh로 저장.

#!/usr/bin/env bash set -euo pipefail

INPUT_PDF="${1:?Usage: compress_pdf.sh input.pdf [screen|ebook|printer|prepress]}"
QUALITY="${2:-ebook}"

DIR="$(dirname "$INPUT_PDF")" BASE="$(basename "$INPUT_PDF" .pdf)"
OUTPUT="$DIR/$BASE-$QUALITY.pdf"

gs -sDEVICE=pdfwrite\
-dCompatibilityLevel=1.4\
-dPDFSETTINGS="/$QUALITY" \
  -dNOPAUSE -dQUIET -dBATCH \
  -sOutputFile="$OUTPUT"\
"$INPUT_PDF"

echo "Compressed PDF created: $OUTPUT"

권한 부여:

chmod +x scripts/compress_pdf.sh

실행:

./scripts/compress_pdf.sh projects/hana-stablecoin-proposal/assets/reference.pdf
ebook
