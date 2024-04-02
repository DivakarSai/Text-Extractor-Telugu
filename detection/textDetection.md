Text Detection: Implement an algorithm to detect regions of interest (ROIs) where the scrolling text is present in each frame.


import cv2
import pytesseract

def detect_text_regions(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to segment the text regions
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours of the text regions
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through the contours and filter out the regions based on size or other criteria
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        roi = image[y:y+h, x:x+w]

        # Perform OCR on the ROI
        text = pytesseract.image_to_string(roi, lang='eng')

        # If the ROI contains scrolling text, process it further or store the information

        # Draw bounding box around the ROI
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image with bounding boxes
    cv2.imshow("Text Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function with the path to your image
detect_text_regions('/path/to/your/image.jpg')

