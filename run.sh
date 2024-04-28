#!/bin/bash
if [ ! -d "venv" ]; then
  python3 -m venv venv
  pip3 install -r requirements
fi
source venv/bin/activate
if [ ! -d "pdf_originals" ]; then
  mkdir pdf_originals
fi
if [ ! -d "pdf_ocr" ]; then
  mkdir pdf_ocr
fi
if [ ! -d "pdf_compressed" ]; then
  mkdir pdf_compressed
fi
python3 convert.py

for filepath in pdf_ocr/*; do
  if [ "${filepath: -4}" == ".pdf" ]; then
    filename=$(basename "$filepath")
    echo "Compressing $filename"
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.6 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=pdf_compressed/"${filename}" "${filepath}"
  fi
done