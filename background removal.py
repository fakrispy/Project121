# import cv2 to capture videofeed
from typing import Tuple
import cv2

import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(0)
bg = 0

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
mountain = cv2.imread('mount everest.jpg')

# resizing the mountain image as 640 X 480
cv2.resize(mountain, (640, 640))

while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([0, 120, 50])
        upper_bound = np.array([10, 255, 255])
        mask_1 = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        # thresholding image

        lower_bound = np.array([170, 120, 70])
        upper_bound = np.array([180, 255, 255])
        mask_2 = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        mask_1 = mask_1 + mask_2

        

        # inverting the mask

        # bitwise and operation to extract foreground / person
        mask_2 = cv2.bitwise_not(mask_1)
        res_1 = cv2.bitwise_and(mountain, mountain, mask = mask_2)
        res_2 = cv2.bitwise_and(bg, bg, mask = mask_1)
        cv2.imshow("result2", res_2)

        # final image

        # show it
        cv2.imshow('frame' , frame)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
