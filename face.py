#!/usr/bin/env python

import cv2
import sys

if len(sys.argv) < 3:
	exit('Usage: facedetect.py infile outfile')

input_file = sys.argv[1]
output_file = sys.argv[2]

face_cascades = (
	cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_default.xml'),
	cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_alt2.xml'),
	cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_alt.xml'),
	cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_alt_tree.xml')
	)
eye_cascades = (
	cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_lefteye_2splits.xml'),
	cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml'),
	cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_eye.xml')
	)


# Function for trying out all the cascades to find a given element
def find_element(img, cascades):
	for cascade in cascades:
		found = cascade.detectMultiScale(img, 1.05, 5)	
		if len(found):
			return found
	return ()

cap = cv2.VideoCapture(input_file)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

frame_num = 0

WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter(output_file, fourcc, 30.0, (WIDTH,HEIGHT))

print("Width x Height: ", WIDTH, HEIGHT)

while(True):
	ret, frame = cap.read()
	frame_num += 1

	if not ret:
		break

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	faces = find_element(gray, face_cascades)
	if not len(faces):
		print("no faces")

	for (x,y,w,h) in faces:
		img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = find_element(roi_gray, eye_cascades)
		if not len(eyes): 
			print("no eyes")
		for (ex,ey,ew,eh) in eyes:
			print("found face and eye(s)")
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	writer.write(frame)
cap.release()
writer.release()




