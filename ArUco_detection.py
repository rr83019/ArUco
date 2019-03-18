import numpy as np
import cv2
import cv2.aruco as aruco
import time
from ArUco_library import *


image_list = ["path_to_directory/Image.png","path_to_directory/Image.png"]
count = 0

for image in image_list:
	img = cv2.imread(image)
	Detected_ArUco_markers = detect_ArUco(img)
	angle = Calculate_orientation_in_degree(Detected_ArUco_markers)
	img = mark_ArUco(img,Detected_ArUco_markers,angle)
	cv2.imwrite("ArUco"+str(count++)+".png",img)

