import numpy as np
import cv2

video = cv2.VideoCapture(0)

while(True):
    ret, frame = video.read()
    resized_video = cv2.resize(frame, (1000, 700))
    cv2.imshow('Video Capture', resized_video)
    if cv2.waitKey(10) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()