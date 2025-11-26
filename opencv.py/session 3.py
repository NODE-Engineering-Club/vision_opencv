#how to capture something from your cam
import numpy as np
import cv2

cap = cv2.VideoCapture(0) #0 is your first video device

while True:
	ret, frame = cap.read()
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows