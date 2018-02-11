import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# Set Constant Image Path
original_image_path = "/Users/Vasukesh/Desktop/Digital-Image-Classwork/Images/roadsign_original.png"
# Read Original Image
img = cv2.imread(original_image_path)
rows,cols,ch = img.shape

# Grab Perspective Points ([Top Right], [Top Left], [Bottom Right], [Bottom Left] )
pts1 = np.float32([[110,59], [213,52], [111,189], [216,186]])
pts2 = np.float32([[0,0], [150,0], [0, 150], [150, 150]])
# Get Perspective From Points
M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(150,150))


plt.title('Original Road Sign')
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()