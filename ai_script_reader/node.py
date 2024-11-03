import cv2
import numpy as np

# Create a blank white image (200x120 pixels)
staff = np.full((120, 200, 3), 255, dtype=np.uint8)  # 3 channels for RGB, filled with 255 (white)

# Draw a vertical line at position (100, 50) to (100, 110) with black color and thickness 2
cv2.line(staff, (100, 50), (100, 110), (0, 0, 0), 2)

# Save the image to a file
cv2.imwrite("node.png", staff)

# Display the image in a window
cv2.imshow("Staff with Line", staff)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()

