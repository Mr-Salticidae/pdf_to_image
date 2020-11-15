#!/usr/bin/env python3

import sys
import os
from pdf2image import convert_from_path
from pathlib import Path
import re

target_format = sys.argv[1]
pdf_file_path = sys.argv[2]
current_folder_path = Path(__file__).parent
try:
    target_folder_path = sys.argv[3]
except:
    target_folder_path = current_folder_path

if os.path.exists(pdf_file_path):
    if os.path.exists(target_folder_path):
        file_name = re.search(r"/(\w+)\.pdf", pdf_file_path).group(1)
        if target_format.lower() == 'png':
            pages = convert_from_path(pdf_file_path)
            for i in range(len(pages)):
                image = pages[i]
                image.save(os.path.join(target_folder_path, file_name + '.png'), 'PNG')
        elif target_format == 'jpg' or target_format == 'JPEG':
            pages = convert_from_path(pdf_file_path)
            for i in range(len(pages)):
                image = pages[i]
                image.save(os.path.join(target_folder_path, file_name + '.jpg'), 'JPEG')
        else:
            print('The first argument shoule be (png | PNG | jpg | JPEG), please try again.')
    else:
        print('Couldn\'t find the target folder, please check the path of the target folder.')
else:
    print('Couldn\'t find the target PDF file, please check the path of the PDF file.')