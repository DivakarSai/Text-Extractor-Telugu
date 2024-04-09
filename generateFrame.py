import cv2


def generate_image_with_bounding_box(frame, scrolling_region):
    # Draw a bounding box on the frame
    x, y, w, h = scrolling_region
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Save the frame as an image
    image_path = "images/sample_image.jpg"  # Replace with the desired path to save the image
    cv2.imwrite(image_path, frame)
    
    return image_path







