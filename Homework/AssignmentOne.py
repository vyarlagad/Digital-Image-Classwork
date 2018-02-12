'''
Name: Vasukesh Yarlagadda
Date: 2/11/2018
Assignment: Homework One Orthographic/Non Orthographic getPerspectiveTransform
'''



import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# Set Constant Image Path
original_image_path = "/Users/Vasukesh/Desktop/Digital-Image-Classwork/Images/Pele.png"
# Create Constant For Marker Thickness
Thickness = 8
# Read Original Image
img = cv2.imread(original_image_path)

# Create Hash Table For Circle Coordinates
lookupTable = {0:(208,66), 1:(473,5), 2:(197,181), 3:(481,299)};

# capture shape of image
rows,cols,ch = img.shape

# Grab Perspective Points ([Top Right], [Top Left], [Bottom Right], [Bottom Left] )
pts1 = np.float32([[208,66], [473,5], [197,181], [481,299]])
# Fixed Control Points
pts2 = np.float32([[0,0], [300,0], [0, 300], [300, 300]])
# Get Perspective From Points
M = cv2.getPerspectiveTransform(pts1,pts2)
# wrap perspective to new dimension
dst = cv2.warpPerspective(img,M,(300,300))


# setting consitant figure size
plt.figure(num=None, figsize=(18, 16), dpi=80, facecolor='w', edgecolor='k')
plt.title('Original Pele')
#indicate Points Used on Original Image
for i in range(0,len(lookupTable)):
  img = cv2.circle(img,lookupTable[i], Thickness, (0,0,255), -1)


plt.subplot(121),plt.imshow(img),plt.title('Original Pele')
# Fix Coloring On Image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(122),plt.imshow(dst),plt.title('Perspective Pele')
# Fix Coloring On Image
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()