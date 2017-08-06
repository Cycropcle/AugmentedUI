'''
Created on 05-Aug-2017

@author: sreram
'''

import numpy as np
import cv2
import tensorflow as tf
import copy



cap = cv2.VideoCapture(1)

print (cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
print (cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

width  = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)


resol = 10
dispFrameList = []

while(True):
    
    
    for i in range(resol):
    
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        
        """
        for i in range(int(height)):
            for j in range (int(width)):
                if frame[i][j][0] >= 170 and frame[i][j][1] <= 170 and frame[i][j][2] <= 170:
                    frame[i][j][0] = 255
                    frame[i][j][1] = 255
                    frame[i][j][2] = 255
                else:
                    frame[i][j][0] = 0
                    frame[i][j][1] = 0
                    frame[i][j][2] = 0
        """
        
        #frame = cv2.GaussianBlur(frame, (15,15), 0)
        
        
        
        lower_redm0 = np.array([0,50,50])
        upper_redm0 = np.array([10,255,255])
        
        lower_redm1 = np.array([170,50,50])
        upper_redm1 = np.array([180,255,255])
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        redRegionOfImage0 = cv2.inRange(hsv, lower_redm0, upper_redm0) 
        redRegionOfImage1 = cv2.inRange(hsv, lower_redm1, upper_redm1)
        
        redRegionOfImage  = redRegionOfImage0 + redRegionOfImage1
        
        dispFrame = hsv.copy()
        dispFrame [np.where(redRegionOfImage == 0)] = 0
        dispFrame [np.where(redRegionOfImage != 0)] = 255
        dispFrameList.append(dispFrame.copy())
        
        
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    
    #dispFrame [:len(dispFrame)][:len(dispFrame[0])] = 0
    
    for i in range(1, resol):
        dispFrameList[0][np.where(dispFrameList[i] == 255)] = 255
    cv2.imshow('frame', dispFrameList[0])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
    dispFrameList = []

    #for i in range(int(width)):
    #    for j in range(int(height)):
    #        print (frame[i][j])
            
        



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
