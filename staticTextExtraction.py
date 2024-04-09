import cv2
import pytesseract
from PIL import Image
from regionofinterest import scrolling_region


frame_gap = 25

# Filter out text clusters with low confidence
def average_confidence_level(extracted_text):
    total_confidence = sum(int(confidence) for confidence in extracted_text["conf"] if extracted_text["text"])
    count = len([text for text in extracted_text["text"] if text.strip()])
    average_confidence = total_confidence / count if count > 0 else 0
    print("average confidence:", average_confidence)
    return average_confidence

def compare_text(text1, text2):
    # convert the text to strings
    text1 = " ".join(text1)
    text2 = " ".join(text2)

    max_length = max(len(text1), len(text2))

    # max_mismatches is the maximum number of mismatches allowed: 40 percent of the length of the longer string
    max_mismatches = int(0.4 * max_length)

    # matching_chars is the number of characters that match in the two strings
    matching_chars = sum(
        1 for char1, char2 in zip(text1, text2) if char1 == char2
    )
    
    # Check if the number of mismatches is within the allowed range
    if max_mismatches >= max_length - matching_chars:
        return True
    else:
        return False


def attatch_lines(text_list, text):
    # case 0: text is empty
    if len(text) == 0:
        return text_list
    
    # case 1: text_list is empty, add text to text_list
    if len(text_list) == 0:
        text_list.append(text)
        return text_list
    
    # case 2: last line in text_list is almost same as text, return text_list
    if compare_text(text_list[-1], text):
        # keep the longer text and discard the shorter one
        if len(" ".join(text_list[-1])) < len(" ".join(text)):
            text_list[-1] = text
        return text_list
    else :
        text_list.append(text)
        return text_list
    




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
    # Perform OCR on the cropped image to get text and confidence
    telugu_text = pytesseract.image_to_data(
        pil_image, config=custom_config, output_type=pytesseract.Output.DICT
    )
    # strip the first and last few characters to avoid noise
    # strip_front, strip_back = stripping_lengths(telugu_text)

    # telugu_text = telugu_text[strip_front:-strip_back]

    return telugu_text


def static_text_from_video(video, window):
    text_list = []
    x, y, w, h = window

    # Read frames from the video
    for i in range(video._get_frame_count()):
        # Read the next frame
        frame = video.frame()

        if frame is None:
            break

        # Extract text from every 10th frame using extract_telugu_text
        if i % 25 == 0:
            telugu_text = text_from_image(frame, (x, y, w, h))
            average_confidence = average_confidence_level(telugu_text)

            if average_confidence < 75:
                continue

            telugu_text = telugu_text["text"]
            # remove empty strings
            telugu_text = [line for line in telugu_text if line.strip()]

            # Append the extracted text to the text_list
            print("current frame:", telugu_text)
            # text_list.append(telugu_text)
            text_list = attatch_lines(text_list, telugu_text)
            print("final list:", text_list)

    stories = []

    # return the final list of text after coneverting into strings
    for text in text_list:
        stories.append(" ".join(text))
    return stories
