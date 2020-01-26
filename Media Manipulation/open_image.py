import cv2

img = cv2.imread('img1.jpg')
resized_img = cv2.resize(img, (800, 600))
cv2.imshow('original', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()