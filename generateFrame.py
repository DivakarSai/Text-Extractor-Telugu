import cv2


def generate_image_with_bounding_box(frame, scrolling_region):
    
    # Create a new image path
    image_path = "images/sample_image.jpg" 
    # Draw a bounding box on the frame
    x, y, w, h = scrolling_region
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    try:
        cv2.imwrite(image_path, frame)
        return image_path
    except Exception as e:
        raise Exception(f"Error saving image: {e}")







