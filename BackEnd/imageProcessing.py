import cv2
import numpy as np

# Load the image
image = cv2.imread('img_folder/cheeseOne.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve edge detection
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred_image, 200, 300) #intensity of edge detection (lower edge, higher edge)

# Find contours based on the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Copy the original image to draw on
output_image = image.copy()

# Loop over the contours and draw bounding boxes around them
for contour in contours:
    area = cv2.contourArea(contour)
    # Filter out small contours to avoid noise
    if 100 < area < 500:  # Adjust as necessary based on the size of curds
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Green bounding box

# Show the output image with detected curds
cv2.imshow('Curd Detection', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




