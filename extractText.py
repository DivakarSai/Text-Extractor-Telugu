import pytesseract
from PIL import Image

def extract_telugu_text(image_path, x, y, w, h):
    # Open the image
    image = Image.open(image_path)
    # Crop the image based on the bounding box
    cropped_image = image.crop((x, y, x + w, y + h))
    # Set the language to Telugu
    custom_config = r'--oem 3 --psm 6 -l tel'
    # Perform OCR on the cropped image
    telugu_text = pytesseract.image_to_string(cropped_image, config=custom_config)
    return telugu_text


