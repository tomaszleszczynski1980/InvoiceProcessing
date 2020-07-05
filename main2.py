# this is the simplest example of usage Tesseract with Python

import cv2
import pytesseract
from pytesseract import Output


img = cv2.imread('images/drezno.jpg')

# all ocr results stored in dictionary

content = pytesseract.image_to_data(img, lang='pol', output_type=Output.DICT)

print(content.keys())

# we can print text (which is list, thus we can easily find particular expression in it)
print(content['text'])

# or join it to have a string
output = " ".join(content['text'])
print(output)

# custom_config = r'--oem 3 --psm 6'
# txt_content = (pytesseract.image_to_string(img, config=custom_config))
#
#
# with open('results/invoice.txt', 'w') as file:
#     file.write(txt_content)
