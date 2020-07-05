# this is the simplest example of usage Tesseract with Python

import cv2
import pytesseract


img = cv2.imread('images/invoice.png')

custom_config = r'--oem 3 --psm 6'
txt_content = (pytesseract.image_to_string(img, config=custom_config))

with open('results/invoice.txt', 'w') as file:
    file.write(txt_content)
