import cv2

def blackhat_image(image):
    # Load the image
    #image = cv2.imread(image_path)

    # Create a structuring element for the blackhat operation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    # Perform the blackhat operation
    blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

    # Save the blackhat image
    #cv2.imwrite("blackhat_image.jpg", blackhat)

    return blackhat

# Example usage
#image_path = "/path/to/image.jpg"
#blackhat_image(image_path)
