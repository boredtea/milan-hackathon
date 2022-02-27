import pytesseract

# path to tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\soumi\AppData\Local\Programs\Tesseract-OCR\tesseract'

imageText = pytesseract.image_to_string(r'C:\Users\soumi\Documents\Code_stuff\Various_Projects\milan-hackathon\amazonPacket2.jpeg')

lines = imageText.split('\n')
lines = ' '.join(lines).split()
print(type(imageText))
print(imageText)
print(lines)