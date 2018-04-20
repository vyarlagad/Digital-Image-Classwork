import numpy as np
import cv2
import matplotlib.pyplot as plt
from data_paths import data_path
from os import fsencode, listdir
from os.path import isfile, join
from time import time
lower_red = np.array([0,100,100])
upper_red = np.array([10, 255, 255])
test_lower = np.array([0,100,100])
test_high  = np.array([10,255,255])
def check_hat(img):
    test = bool(mask[30,176]/255)
    if test:
        return 'has'
    else:
        return 'Does not have'
def check_label(img, res, mask):
    if(res[191,176,2]==0 and np.sum(res[270,140:180,2])!=0):
        return 'has slipped'
    elif(img[189,176,2] < 50):
        return 'is missing'
    elif(np.sum(mask[191,140:170]) == 0):
        return 'is white'
    else:
        return 'is correct'
def check_missing(res):
    if(np.sum(res[:,176, 2])):
        return False
    else:
        return True
def check_fill(hsv):
    test = cv2.threshold(hsv[:,:,1], 185, 255, cv2.THRESH_BINARY)[1]
    
    if(np.sum(test[120,140:170]) != 0):
        return 'overfilled'
    elif(np.sum(test[141,140:190]) != 0):
        return 'correctly filled'
    else:
        return 'underfilled'

onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]
cap  = 55
folder = fsencode(data_path)
img  = cv2.imread(data_path + 'image001.jpg', 1)
t0 = time()
for n in range(0, len(onlyfiles)):
        img = cv2.imread(join(data_path,onlyfiles[n]),1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(img,img, mask= mask)    
        hat = check_hat(mask)
        label = check_hat(mask)
        fill = check_fill(hsv)
       # if(not(check_missing(res))):
            #print ('Bottle', n+1, hat  + ' a hat', 'The label ' + label + 'and is ' + fill)
       # else:
            #print('Bottle', n+1, 'is missing')
dt = time() - t0
print('141 pictures in ' + str(dt) + 's', 'at a rate of ', float(n/dt), 'frames/second')

img = cv2.imread(data_path + 'image078.jpg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(np.amax(hsv[141,140:190]))
mask = cv2.inRange(hsv, test_lower, test_high)
res = cv2.bitwise_and(img,img, mask= mask)

plt.imshow(hsv, cmap='gray')

plt.show()

