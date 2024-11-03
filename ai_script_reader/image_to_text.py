from PIL import Image
import pytesseract

# Path to the image
image_path = 'music_sheet.jpg'

# Load the image
image = Image.open(image_path)

# Use pytesseract to extract text
#text = pytesseract.image_to_string(image)
#text = pytesseract.image_to_alto_xml(image)
#text = pytesseract.image_to_boxes(image)
#text = pytesseract.image_to_data(image)
text = pytesseract.image_to_osd(image)

# Print the extracted text
print(text)

