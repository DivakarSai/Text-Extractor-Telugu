Text Extraction: Develop a method to extract the text from the detected ROIs accurately.

import pytesseract
from PIL import Image

def extract_telugu_text(image_path):
    # Open the image
    image = Image.open(image_path)

    # Set the language to Telugu
    custom_config = r'--oem 3 --psm 6 -l tel'

    # Perform OCR on the image
    telugu_text = pytesseract.image_to_string(image, config=custom_config)

    return telugu_text

# Usage example
image_path = '/path/to/your/image.png'
telugu_text = extract_telugu_text(image_path)
print(telugu_text)



# learning so far
ఎన్నికల is a string of length 7 where న్ని has 4 charecters 'న', '్', 'న', 'ి'