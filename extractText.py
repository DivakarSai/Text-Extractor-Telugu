import pytesseract
from PIL import Image
import numpy as np
import cv2

def stripping_lengths(text):

    default_len = 5

    if(len(text)<default_len):
        return 0, 0
        return len(text/2), len(text/2)
    else:
        return default_len, default_len
    
    
    #return len(text.strip()/5)

def extract_telugu_text(image, x, y, w, h):

    # get roi from image
    roi = image[y:y+h, x:x+w]

    # do gray scale

    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Perform thresholding
    _, thresholded_roi = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


    # Convert the image to PIL format
    pil_image = Image.fromarray(thresholded_roi)


    # Set the language to Telugu
    custom_config = r'--oem 3 --psm 6 -l tel'
    # Perform OCR on the cropped image
    telugu_text = pytesseract.image_to_string(pil_image, config=custom_config)


    # strip the first and last few characters to avoid noise
    strip_front, strip_back = stripping_lengths(telugu_text)

    telugu_text = telugu_text[strip_front:-strip_back]

    

    return telugu_text


