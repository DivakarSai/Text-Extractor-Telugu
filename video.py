"""
Module for working with video files.
"""

import cv2


class Video:
    """Class for working with video files."""

    def __init__(self, path, language="Telugu"):
        """
        Initialize the Video object.

        Parameters:
            path (str): Path to the video file.
            ocr (OCR object, optional): OCR object for language detection.
            language (str, optional): Default language for OCR. Defaults to "Telugu".
        """
        self.video_capture = cv2.VideoCapture(path)
        self.frame_rate = self.video_capture.get(cv2.CAP_PROP_FPS)
        self.frame_count = self._get_frame_count()
        self.height = int(self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.width = int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.shape = [self.height, self.width, 3]
        if language is not None:
            self.language = language

    def __del__(self):
        """Destructor to release video capture resources."""
        del self.video_capture

    def _get_frame_count(self):
        """
        Get the total number of frames in the video.

        Returns:
            int: Total number of frames.
        """
        frame_count = 0
        while self._got_frame():
            frame_count += 1
        self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        return frame_count

    def _got_frame(self):
        """
        Check if there's a frame available in the video capture.

        Returns:
            bool: True if frame is available, False otherwise.
        """
        success, _ = self.video_capture.read()
        return success

    def frame(self, frame_number=None):
        """
        Get a specific frame from the video.

        Parameters:
            frame_number (int, optional): Frame number to retrieve. Defaults to None.

        Returns:
            numpy.ndarray or None: Image data of the frame, or None if frame retrieval fails.
        """
        if frame_number is not None:
            self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        read_success, image = self.video_capture.read()
        if not read_success:
            return None
        return image
    