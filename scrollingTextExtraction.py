import cv2
import pytesseract
from PIL import Image
from regionofinterest import scrolling_region


frame_gap = 25


# Filter out text clusters with low confidence
def filter_text_clusters(extracted_text, confidence_threshold=75):
    filtered_clusters = []
    for i in range(len(extracted_text["text"])):
        text = extracted_text["text"][i].strip()
        if text:
            confidence = int(extracted_text["conf"][i])
            if confidence >= confidence_threshold:
                filtered_clusters.append((text, confidence))

    # return normal text
    return " ".join([text for text, _ in filtered_clusters])


def attatch_strings(text1, text2):
    # case 0: text1 is empty, return text2
    if len(text1) == 0:
        return text2
    if len(text2) == 0:
        return text1
    # case 1: last words in text1 and text2 are the same , return text2
    if len(text2)>=1 and text1[-1] == text2[-1]:
        return text1
    # case 2: last words in text1 is the penultimate word in text2, add the last wors to text2
    elif len(text2)>=2 and text1[-1] == text2[-2]:
        return text1 + text2[-1:]
    # case 3: search for the last word of text1 in text2 if found, add the words to the right of the penultimate word in text2 to text1 after removing the last word from text1
    elif text1[-2] in text2:
        # search the index of the last word of text1 in text2 if threre are multiple occurences, choose the last one
        index = -1
        for i, word in enumerate(text2):
            if word == text1[-2]:
                index = i
        return text1[:-1] + text2[index + 1 :]
    # case 4: serach for the last word in text1 in text2, if found, remove the last word in text1
    elif text1[-2] not in text2:
        return text1[:-1] + text2


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


def scrolling_text_from_video(video, window):
    final_string = ""
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
            telugu_text = telugu_text["text"]
            # remove last word
            if len(telugu_text) > 0:
                telugu_text = telugu_text[:-1]
            # remove empty strings
            telugu_text = [line for line in telugu_text if line.strip()]

            # Append the extracted text to the text_list
            print("current frame:", telugu_text)
            # text_list.append(telugu_text)
            final_string = attatch_strings(final_string, telugu_text)
            print("final string:", final_string)

    final_string = " ".join(final_string)
    return final_string
