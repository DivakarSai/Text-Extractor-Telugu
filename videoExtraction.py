import cv2
from extractText import extract_telugu_text
from stitchText import stitch_strings
from region import scrolling_region

x, y, w, h = scrolling_region



frame_gap = 50

def capture_video(video_path):
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was successfully opened
    if not cap.isOpened():
        print("Error opening video file")
        exit()

    return cap


def video_properties(cap):
    # Get the video properties
    # Get the frames per second
    fps = cap.get(cv2.CAP_PROP_FPS)
    # Get the width and height of frame
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    return fps, width, height, count


def text_from_video(cap, frame_count):

    # Initialize an empty list to store the extracted text from each frame
    # text_list = []
    final_string = ""


    # Read frames from the video
    for i in range(frame_count):
        # Read the next frame
        ret, frame = cap.read()

        # Check if the frame was successfully read
        if not ret:
            break

        # Extract text from every 10th frame using extract_telugu_text
        if i % frame_gap == 0:
            telugu_text = extract_telugu_text(frame, x, y, w, h)

            # Append the extracted text to the text_list
            # print("current frame:", telugu_text)
            # text_list.append(telugu_text)
            final_string = stitch_strings(final_string, telugu_text)



    return final_string