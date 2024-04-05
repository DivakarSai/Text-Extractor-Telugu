import cv2

def capture_video(video_path):
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was successfully opened
    if not cap.isOpened():
        print("Error opening video file")
        exit()

    return cap
