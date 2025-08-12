import numpy as np
import cv2

colors_to_detect = {
    "Yellow": [0, 255, 255],
    "Red": [0, 0, 255],
    "Blue": [255, 0, 0],
    "Green": [0, 255, 0]
}

def get_limits(color_bgr):
    
    c= np.uint8([[color_bgr]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] -10, 100, 100
    upperLimit = hsvC[0][0][0] +10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype= np.uint8)
    upperLimit = np.array(upperLimit, dtype= np.uint8)

    return lowerLimit, upperLimit