import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt


# Read In image and convert to grayscale
img = cv2.imread('cloth_0199.jpg', 0)
plt.imshow(img)


# kernel Structuring Element
kernel = np.ones((5,5),np.uint8)

# Morphological Closed Image
morph_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# Morphological Open Image (Erosion followed by dialation)
morph_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Binary Thresholding
thresh = cv2.threshold(morph_close, 127, 255, cv2.THRESH_BINARY_INV)
plt.imshow(thresh)

# Find the contours
img2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
plt.imshow(img2)


# Draw the contours of an image ( We Dont know how many to expect)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
plt.imshow(img)
plt.show()
