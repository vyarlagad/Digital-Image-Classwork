import numpy as np
import cv2
import matplotlib.pyplot as plt
from detection_funct import *
from os import fsencode, listdir, fsdecode
from os.path import isfile, join
from time import time, sleep

data_path = 'C:/Users/vyarlaga/Desktop/Digital-Image-Classwork/Homework/Homework 6/cocacolaPic/'


# Thresholding based off color , used for detecting the color red
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])


# Set Timer to indicate time take per image
t0 = time()

plt.ion()
for file in listdir(data_path):
    filename = fsdecode(file)
    print(filename)
    if filename.endswith(".jpg"):
        img = cv2.imread(join(data_path, filename), 1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(img, img, mask=mask)
        hat = check_hat(mask)
        process_result(hat, 4)  # get result from hat function
        label = check_label(img, res, mask)
        process_result(label, 1)  # get result from label function
        fill = check_fill(hsv)
        process_result(fill, 2)  # get result from fill function
        cv2.imshow('bottle',img)
        if cv2.waitKey(1) == ord('q'):
            break

    else:
        continue

    dt = time() - t0
print('time taken ', dt)

img = cv2.imread(data_path + 'image078.jpg', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(np.amax(hsv[141, 140:190]))
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('bush did 911',hsv)
