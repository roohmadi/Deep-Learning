# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 21:15:00 2022

@author: Predator
"""


import cv2

#webcam
#cap = cv2.VideoCapture(0)
#CCTV
cap = cv2.VideoCapture("rtsp://admin:admin82@192.168.1.3:554/unicast/c1/s0/live")

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
	#https://stackoverflow.com/questions/52162004/i-am-having-trouble-with-this-error-215assertion-failed-ssize-empty-in-fu
	try:
		ret, frame = cap.read()
		frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
		cv2.imshow('Input', frame)
	except Exception as e:
		print(str(e))

	c = cv2.waitKey(1)
	if c == 27:
		break

cap.release()
cv2.destroyAllWindows()