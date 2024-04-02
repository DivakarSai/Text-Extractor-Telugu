import cv2
import pytesseract

def detect_scrolling_region(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to segment the text regions
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours of the text regions
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # remove small contours
    contours = [c for c in contours if cv2.contourArea(c) > 10000]

    # select the bottom-most contour
    bottom_contour = max(contours, key=lambda c: cv2.boundingRect(c)[1])

    # Iterate through the contours and filter out the regions based on size or other criteria
    # for contour in contours:
    x, y, w, h = cv2.boundingRect(bottom_contour)
    roi = image[y:y+h, x:x+w]

    # Perform OCR on the ROI
    text = pytesseract.image_to_string(roi, lang='tel')

    # If the ROI contains scrolling text, process it further or store the information

    # Draw bounding box around the ROI
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image with bounding boxes
    cv2.imshow("Text Detection", image)
    cv2.waitKey(5000)




