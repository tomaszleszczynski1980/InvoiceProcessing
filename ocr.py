# this is the simplest example of usage Tesseract with Python
# adapted as command line tool

import cv2
import pytesseract
from sys import argv


if len(argv) > 1:
    image_file = argv[1]

else:
    image_file = input('Image file path>>> ')

try:
    img = cv2.imread(image_file)
    custom_config = r'--oem 3 --psm 6'
    txt_content = (pytesseract.image_to_string(img, config=custom_config))

    with open(image_file + '.txt', 'w') as file:
        file.write(txt_content)

except FileNotFoundError:
    print(f'{argv[1]} not found')

except TypeError as error:
    print(error)
