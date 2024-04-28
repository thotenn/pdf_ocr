sudo apt-get update
sudo apt-get install libleptonica-dev:i386 tesseract-ocr libtesseract-dev:i386 tesseract-ocr-eng tesseract-ocr-script-latn

On Mac
brew install tesseract

On Windows
download binary from https://github.com/UB-Mannheim/tesseract/wiki. then add pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' to your script.

Then you should install python package using pip:
pip install tesseract
pip install tesseract-ocr


sudo apt install autotools-dev automake libtool libleptonica-dev
sudo apt-get install git autoconf automake libtool

git clone https://github.com/agl/jbig2enc.git
cd jbig2enc
./autogen.sh
./configure
make
sudo make install

git clone https://github.com/agl/jbig2enc.git
cd jbig2enc
./autogen.sh
./configure
make
sudo make install

sudo apt-get install pngquant



para comprimir los pdf
sudo apt install ghostscript
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.6 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=compressed.pdf b.pdf
