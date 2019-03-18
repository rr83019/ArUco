import numpy as np
import cv2
import cv2.aruco as aruco
import time
from ArUco_library import *


init = time.time()
cap = cv2.VideoCapture('input_video.avi')

while(cap.isOpened()):
	ret,img=cap.read()
	Detected_ArUco_markers = detect_ArUco(img
	angle = Calculate_orientation_in_degree(Detected_ArUco_markers)
	img = mark_ArUco(img,Detected_ArUco_markers,angle)

	cv2.imshow('vid_frame',img)			
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		exit(0)

cap.release()
cv2.destroyAllWindows()
print(time.time()-init)

