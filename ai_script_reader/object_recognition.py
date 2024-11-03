import cv2
import numpy as np

# Load the main image and template image
main_image = cv2.imread('sheet.jpg')
template = cv2.imread('do.png', cv2.IMREAD_GRAYSCALE)

main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(main_gray, template, cv2.TM_CCOEFF_NORMED)

# Specify a threshold
threshold = 0.5
loc = np.where(result >= threshold)

print(loc)

# Draw rectangles around matched regions
for pt in zip(*loc[::]):
    cv2.rectangle(main_image, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)

# Display the result
cv2.imwrite('my_do.png', main_image)
cv2.imshow('Template Matching', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
