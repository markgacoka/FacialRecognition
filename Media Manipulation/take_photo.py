import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret,frame = cap.read()

while(True):
    cv2.imshow('Photo capture',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite('img.png',frame)
        cv2.destroyAllWindows()
        break

cap.release()