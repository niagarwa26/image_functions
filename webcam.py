#!/usr/bin/python3

import cv2


#now starting cam

cap = cv2.VideoCapture(0)

while cap.isOpened() :
	print ("camera is working")
	status,frame = cap.read()
	cv2.imshow("camera0",frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imwrite("new.jpg",frame)
		cv2.destroyAllWindows()
		cap.release()
