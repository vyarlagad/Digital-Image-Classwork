import numpy as np
import cv2
import matplotlib.pyplot as plt
from detection_funct import *
from os import fsencode, listdir, fsdecode
from os.path import isfile, join
from time import time

data_path = 'C:/Users/Timothy/Digital-Image-Classwork/Homework/Homework 6/cocacolaPic/'


lower_red = np.array([0,100,100])
upper_red = np.array([10, 255, 255])
test_lower = np.array([0,100,100])
test_high  = np.array([10,255,255])


'''files = [f for f in listdir(data_path) if isfile(join(data_path,f))]
cap  = 55
folder = fsencode(data_path)
img  = cv2.imread(data_path + 'image001.jpg', 1)
'''
# Set Timer to indicate time take per image
t0 = time()

directory = fsencode(data_path)

for file in listdir(data_path):
    filename = fsdecode(file)
    print(filename)
    if filename.endswith(".jpg"):
        img = cv2.imread(join(data_path,filename),1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(img,img, mask= mask)
        hat = check_hat(mask)
        process_result(hat,4) # get result from hat function
        label = check_label(img, res, mask)
        process_result(label,1) # get result from label function
        fill = check_fill(hsv)
        process_result(fill, 2) # get result from fill function
        dt = time() - t0
    else:
        continue

dt = t0 - time()
print('time taken ', dt)

img = cv2.imread(data_path + 'image078.jpg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(np.amax(hsv[141,140:190]))
mask = cv2.inRange(hsv, test_lower, test_high)
res = cv2.bitwise_and(img,img, mask= mask)

plt.imshow(hsv, cmap='gray')

plt.show()