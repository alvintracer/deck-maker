#!/usr/bin/env bash
set -euo pipefail

INPUT_PDF="${1:?Usage: compress_pdf.sh input.pdf [screen|ebook|printer|prepress]}"
QUALITY="${2:-ebook}"

DIR="$(dirname "$INPUT_PDF")"
BASE="$(basename "$INPUT_PDF" .pdf)"
OUTPUT="$DIR/$BASE-$QUALITY.pdf"

gs -sDEVICE=pdfwrite \
  -dCompatibilityLevel=1.4 \
  -dPDFSETTINGS="/$QUALITY" \
  -dNOPAUSE -dQUIET -dBATCH \
  -sOutputFile="$OUTPUT" \
  "$INPUT_PDF"

echo "Compressed PDF created: $OUTPUT"