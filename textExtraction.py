import cv2
import pytesseract
from PIL import Image


frame_gap = 50

def stitch_strings(first_string, second_string):


    # Convert the strings to lowercase for case-insensitive matching
    first_string = first_string.lower()
    second_string = second_string.lower()

    # Iterate through the first string to find the common suffix
    common_suffix = ''
    for i in range(len(first_string)):
        if second_string.startswith(first_string[i:]):
            common_suffix = first_string[i:]
            break
    
    # If a common suffix is found, combine the strings using it
    if common_suffix:
        return first_string + second_string[len(common_suffix):]
    else:
        # If no common pattern is found, just concatenate the strings
        return first_string + second_string



def stripping_lengths(text):
    default_len = 5

    if len(text) < default_len:
        return 0, 0
    return default_len, default_len


def text_from_image(image, window):
    x, y, w, h = window

    # get roi from image
    roi = image[y : y + h, x : x + w]

    # do gray scale

    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Perform thresholding
    _, thresholded_roi = cv2.threshold(
        gray_roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Convert the image to PIL format
    pil_image = Image.fromarray(thresholded_roi)

    # Set the language to Telugu
    custom_config = r"--oem 3 --psm 6 -l tel"
    # Perform OCR on the cropped image
    telugu_text = pytesseract.image_to_string(pil_image, config=custom_config)

    # strip the first and last few characters to avoid noise
    strip_front, strip_back = stripping_lengths(telugu_text)

    telugu_text = telugu_text[strip_front:-strip_back]

    return telugu_text


def text_from_video(video, window):
    # Initialize an empty list to store the extracted text from each frame
    # text_list = []
    final_string = ""
    x, y, w, h = window

    # Read frames from the video
    for i in range(video._get_frame_count()):
        # Read the next frame
        frame = video.frame()

        if frame is None:
            break

        # Extract text from every 10th frame using extract_telugu_text
        if i % frame_gap == 0:
            telugu_text = text_from_image(frame, (x, y, w, h))

            # Append the extracted text to the text_list
            # print("current frame:", telugu_text)
            # text_list.append(telugu_text)
            final_string = stitch_strings(final_string, telugu_text)

    return final_string
