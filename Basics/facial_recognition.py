#Importing the OpenCV Library
import cv2

#Loading images in OpenCV
img = cv2.imread("Images\\DSCN4569.JPG", 1) #Loads an RGB image
img2 = cv2.imread("\\Images\\DSCN4569.JPG", 0) #Loads a grayscale image
print(img.shape) #Prints the dimensions and channels present (pix length, pix w, rgb?)

print(img) #Prints a numpy array of the image 3D matrix if RGB and 2D matrix if grayscale

# Displaying the image
cv2.imshow("DSCN4569", img) #Displays the image file
cv2.waitKey(0) #waits for key input and closes the window
cv2.waitKey(2000) #waits for 2000 milliseconds and closes the window
cv2.destroyAllWindows() #Close the image window

#Resizing the image
resized = cv2.resize(img, (600, 600))
cv2.imshow("DSCN4569", resized)
cv2.waitKey(2000) #waits for 2000 milliseconds and closes the window
cv2.destroyAllWindows() #Close the image window
# More robust method
resized2 = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2))) #resize the image by diving its dimensions in half
cv2.imshow("DSCN4569", resized) #Display the resized image
cv2.waitKey(2000) #wait for 2000 ms and close

# Face Detection
# Create a cascade classifier that will contain the features of the face
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #Classifier used to detect faces, in this case it only detect front faces
img = cv2.imread("DSCN4601.JPG") #reads the image file and stores it in img
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #changes the colored image to grayscale
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 50) #runs cascade classifiers with high probability of face detection

for x, y, w, h in faces: #for the coordinates around a face
	img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3) #draw a rectangle around the face

resized = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/7))) #resize the image to fit an acceptable size (divided by 7)
cv2.imshow("Photo", resized) #Display the resized photo
cv2.waitKey(0) #wait for a key to be pressed
cv2.destroyAllWindows()  #in order to close the video

#Capture the first frame (the first picture that comes up during a video) of a video
import cv2, time

# Remember to set priorities if it gives an error: setx OPENCV_VIDEOIO_PRIORITY_MSMF 0
video = cv2.VideoCapture(0, cv2.CAP_DSHOW) #reads a video input. Number means webcam or external camera while path name to a video reads video file
check, frame = video.read() #frame is a numpy array that takes the value of the first captured image, check is a Boolean value that checks if frame is present
time.sleep(3) #wait for 3 seconds
cv2.imshow('Video Capture', frame)
cv2.waitKey(0)
video.release() #releases the camera after some milliseconds
cv2.destroyAllWindows() #destroys all active windows

#Capturing Video
# A video is a series of images captured in frames
import cv2, time

#It will capture the video using a while loop where if check is True, the frames will keep on registering
video = cv2.VideoCapture(0, cv2.CAP_DSHOW) #reads a video input. Number means webcam or external camera while path name to a video reads video file
check, frame = video.read() #frame is a numpy array that takes the value of the first captured image, check is a Boolean value that checks if frame is present

a = 1 #variable a will count the number of frames

while True: #while the loop is True
	a += 1 #increment frame count by 1
	check, frame = video.read() #start video input checking if frame is present
	gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting the video to grayscale
	cv2.imshow('Video Capture', frame) #display the video by each frame

	key = cv2.waitKey(1) #wait for a key to be pressed for an action
	if key == ord('q'): #if q is pressed
		break #break out of the loop

print(a) #print the number of frames
video.release() #release the video capture
cv2.destroyAllWindows() #close all active windows
