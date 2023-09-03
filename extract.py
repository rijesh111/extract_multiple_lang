import pytesseract
from PIL import Image

#  path to the Tesseract OCR 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#image containing text in multiple languages
image = Image.open('la.jpg')


languages = 'nep+spa'

# extract text from the image with multiple languages
text = pytesseract.image_to_string(image, lang=languages)

# Print the extracted text
print('Extracted text:', text)


