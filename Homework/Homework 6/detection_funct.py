import numpy as np
import cv2
# func key is 4
def check_hat(mask):
    test = bool(mask[30,176]/255)
    if test:
        return 1
    else:
        return -1

# func key is 1
def check_label(img, res, mask):
    if(res[191,176,2]==0 and np.sum(res[270,140:180,2])!=0):
        return -1 #has slipped
    elif(img[189,176,2] < 50):
        return  0 #is missing
    elif(np.sum(mask[191,140:170]) == 0):
        return  1#is white
    else:
        return  2 #is correct

# func key is 3
def check_missing(res):
    if(np.sum(res[:,176, 2])):
        return False
    else:
        return True

# func key is 2
def check_fill(hsv):
    test = cv2.threshold(hsv[:,:,1], 185, 255, cv2.THRESH_BINARY)[1]

    if(np.sum(test[120,140:170]) != 0):
        return  -1 #'overfilled'
    elif(np.sum(test[141,140:190]) != 0):
        return  0 #'correctly filled'
    else:
        return  1 #'underfilled'


def process_result(result, funcKey):
    if(funcKey == 1): # label
        if(result == -1):
            print("label has slipped")
        elif(result == 0):
            print("label is missing")
        elif(result == 1):
            print("label is white")
        elif(result == 2):
            print("label is correct")
    elif(funcKey == 2): # fill
        if(result == -1):
            print("bottle is overfilled")
        elif(result == 0):
            print("bottle correctly filled")
        elif(result == 1):
            print("bottle is underfilled")
    elif(funcKey == 3): # check missing
        if(result):
            print(" Bottle is not there")
        else:
            print("bottle is there")
    elif(funcKey == 4):
        if(result == -1):
            print("bottle does not have hat")
        elif(result == 1):
            print("bottle has hat")
    else:
        print("Function Not Defined")
