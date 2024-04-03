import pytesseract
from PIL import Image
import numpy as np


def stripping_lengths(text):

    default_len = 5

    if(len(text)<default_len):
        return len(text/2), len(text/2)
    else:
        return default_len, default_len
    
    
    #return len(text.strip()/5)

def extract_telugu_text(image, x, y, w, h):
    # Convert the numpy array to PIL Image
    image = Image.fromarray(image)
    # Crop the image based on the bounding box
    cropped_image = image.crop((x, y, x + w, y + h))
    # Set the language to Telugu
    custom_config = r'--oem 3 --psm 6 -l tel'
    # Perform OCR on the cropped image
    telugu_text = pytesseract.image_to_string(cropped_image, config=custom_config)


    # strip the first and last few characters to avoid noise
    strip_front, strip_back = stripping_lengths(telugu_text)

    telugu_text = telugu_text[strip_front:-strip_back]

    

    return telugu_text


