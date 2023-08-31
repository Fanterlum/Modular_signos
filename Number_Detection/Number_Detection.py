# Made of By Dexne
# Number detection

# Instructions to execute this code
# If you are working in a linux system follow this commands

# Open a new terminal and write:

# Sudo apt update
# sudo apt install tesseract-ocr
# sudo apt install tesseract-ocr-eng tesseract-ocr-fra tesseract-ocr-deu tesseract-ocr-spa
# tesseract --version

# now let's download the library

# pip install pytesseract

import pytesseract
from PIL import Image

# Path to the Tesseract executable (this might be different on your system)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Load the image using PIL (Python Imaging Library)
image_path = 'img/3.JPG'
image = Image.open(image_path)

# Use pytesseract to extract text from the image
result = pytesseract.image_to_string(image, config='--psm 6')
# We are using the image_to_string function from pytesseract 
# to extract the text from the image given.
# Image = is the input from wihich you want to extract text. It should be a PIL (Python Imaging Library)
# Config = this parameter allow yoiu to provide configuration options to tesseract OCR engine
# --psm  flag stands for "Page Segmentation Mode" which controls how Tesseract interprets the layout image


# Process the result to extract numbers
numbers = [int(num) for num in result.split() if num.isdigit()]

print("Extracted numbers:", numbers)
