import cv2

# constants
convert_to_hsv=False
scale_factor = 0.5

def preprocess_image(image):

    # Step 1. Convert to HSV color space 
    if convert_to_hsv:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    # Step 2. Scale down image
    image = cv2.resize(image,(int(image.shape[1]*scale_factor), int(image.shape[0]*scale_factor)))

    return image