import numpy as np
import cv2
import matplotlib.pyplot as plt
from detection_funct import *
from os import fsencode, listdir
from os.path import isfile, join
from time import time

path = '/cocacolaPic'


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

directory = os.fsencode(path)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg"):
        img = cv2.imread(join(data_path,onlyfiles[n]),1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(img,img, mask= mask)
        hat = check_hat(mask)
        label = check_label(mask)
        fill = check_fill(hsv)
        dt = time() - t0
    else:
        continue


print('time taken ', dt)

img = cv2.imread(data_path + 'image078.jpg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(np.amax(hsv[141,140:190]))
mask = cv2.inRange(hsv, test_lower, test_high)
res = cv2.bitwise_and(img,img, mask= mask)

plt.imshow(hsv, cmap='gray')

plt.show()