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