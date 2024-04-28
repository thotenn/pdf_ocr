# import libraries
import os
import shutil
import ocrmypdf
import pandas as pd
import fitz #!pip install PyMuPDF

OCR_PREFIX = 'OCR_'
# get pdf files
PATH = os.getcwd()
PATH_OCR = PATH + '/pdf_ocr/'
PATH_ORIGINAL = PATH + '/pdf_originals/'

file_list = [f for f in os.listdir(path=PATH_ORIGINAL) if f.endswith('.pdf') or f.endswith('.PDF')]

'''
main ocr code, which create new pdf file with OCR_ ahead its origin filename, 
and error messege can be find in error_log
'''

error_log = {}
for file in file_list:
    try:
        print('Processing file: ', file)
        result = ocrmypdf.ocr(
            PATH_ORIGINAL + file,
            PATH_ORIGINAL + OCR_PREFIX + file,
            output_type='pdf',
            skip_text=True,
            deskew=False
        )
    except Exception as e:
        if hasattr(e, 'message'):
            error_log[file] = e.message
        else:
            error_log[file] = e
        continue

'''
extract OCRed PDF using PyMuPDF and save into a pandas dataframe
'''
ocr_file_list = [f for f in os.listdir(path=PATH_ORIGINAL) if f.startswith(OCR_PREFIX)]

# PDF extraction
# informations we want to extract
extraction_pdfs = {}

for file in ocr_file_list:
    print('Rebuilding file: ', file.replace(OCR_PREFIX, ''))
    #save the results
    pages_df = pd.DataFrame(columns=['text'])
    # file reader
    doc = fitz.open(PATH_ORIGINAL + file)
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        pages_df = pages_df._append({'text': page.get_text('text')}, ignore_index=True)
    extraction_pdfs[PATH_ORIGINAL + file] = pages_df

# itera sobre todos los archivos en la carpeta de origen
for filename in os.listdir(PATH_ORIGINAL):
    if filename.startswith(OCR_PREFIX):  # verifica si el nombre del archivo comienza con 'OCR_'
        # mueve el archivo a la carpeta de destino
        shutil.move(PATH_ORIGINAL + filename, PATH_OCR + filename)

# cambia el nombre de los archivos en la carpeta de destino
for filename in os.listdir(PATH_OCR):
    if filename.startswith(OCR_PREFIX):
        new_filename = filename.lstrip(OCR_PREFIX)  # Elimina 'OCR_' del nombre del archivo
        # renombra el archivo
        os.rename(PATH_OCR + filename, PATH_OCR + new_filename)
