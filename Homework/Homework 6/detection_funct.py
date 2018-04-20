import numpy as np
import cv2

# func key is 1
'''
Description: Checks label by taking the restored image and the mask itself. It checks the states slipped, missing, white, correct
Image is BGR.
'''

def check_label(img, res, mask):
    if(res[191, 176, 2] == 0 and np.sum(res[270, 140:180, 2]) != 0):
        return -1  # has slipped
    elif(img[189, 176, 2] < 50):
        return 0  # is missing
        # if the image value is low 
    elif(np.sum(mask[191, 140:170]) == 0):
        return 1  # is white
    else:
        return 2  # is correct

# func key is 2
'''
Description: Used saturation because the image has high saturation where the coke is because its tasty.
Took the saturation channel and then thresholded it so it can be over 185 
'''

def check_fill(hsv):
    test = cv2.threshold(hsv[:, :, 1], 185, 255, cv2.THRESH_BINARY)[1]

    if(np.sum(test[120, 140:170]) != 0):
        return -1  # 'overfilled'
    elif(np.sum(test[141, 140:190]) != 0):
        return 0  # 'correctly filled'
    else:
        return 1  # 'underfilled'

# func key is 3

'''
Description: took a line at the center of the image ( a vertical line) and summed all the values which  is compared for 0 (False) or 1 (True)...swag
'''
def check_missing(res):
    if(np.sum(res[:, 176, 2]) == 0):
        return False
    else:
        return True

'''
Description: Took the mask and used a middle point of the cap and if point exists then return true else we return false ... money
'''
# func key is 4
def check_hat(mask):
    test = bool(mask[30, 176]/255)
    if test:
        return 1
    else:
        return -1

'''
Take integer variables and the function key which is defined by the set of equations  in which the result is presented
'''
def process_result(result, funcKey):
    if(funcKey == 1):  # label
        if(result == -1):
            print("label has slipped")
        elif(result == 0):
            print("label is missing")
        elif(result == 1):
            print("label is white")
        elif(result == 2):
            print("label is correct")
    elif(funcKey == 2):  # fill
        if(result == -1):
            print("bottle is overfilled")
        elif(result == 0):
            print("bottle correctly filled")
        elif(result == 1):
            print("bottle is underfilled")
    elif(funcKey == 3):  # check missing
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
