import numpy as np
import cv2
import cv2.aruco as aruco
import sys
import math
import time


def detect_ArUco(img):
	Detected_ArUco_markers = dict()
	try:
		aruco_dict=aruco.Dictionary_get(aruco.DICT_5X5_250)
		parameters=aruco.DetectorParameters_create()
		corners,ids,_=aruco.detectMarkers(img,aruco_dict,parameters=parameters)
		ids_cor = dict()
		ids2 = []
		cor2 = []
		cor3 = []
		for i in ids:
			ids2.append(i[0])

		for i in corners:
			cor2.append(i)

		for i in cor2:
			cor3.append(i[0])


		for i,j in zip(ids2,cor3):
			Detected_ArUco_markers[i] = j

	except:
		pass

	
	return Detected_ArUco_markers	


def Calculate_orientation_in_degree(Detected_ArUco_markers):
	ArUco_marker_angles = dict()
	angle = []
	try:
		def detect_angle(x1,y1,x2,y2):
			try:
				val = (y2-y1)/(x2-x1)
				val = math.atan(abs(val))
				val = ((int)(val* 180/3.1416))%360
				val = 360 - val
				if(x2<x1 and y2>y1):
					val = (180 - val)%360 
				elif(x2<x1 and y1>y2):
					val = (180 + val)%360
				elif(x2>x1 and y2>y1):
					pass
				elif(x2>x1 and y2<y1):
					val = (360 - val)%360
				return val
			except:
				pass
		for p in Detected_ArUco_markers.keys():
			try:
				x1 = Detected_ArUco_markers[p][0][0]
				y1 = Detected_ArUco_markers[p][0][1]

				x2 = Detected_ArUco_markers[p][1][0]
				y2 = Detected_ArUco_markers[p][1][1]

				x3 = Detected_ArUco_markers[p][2][0]
				y3 = Detected_ArUco_markers[p][2][1]

				x4 = Detected_ArUco_markers[p][3][0]
				y4 = Detected_ArUco_markers[p][3][1]

				x, y = 0.5*abs(x3+x1),0.5*abs(y3+y1)
				x5, y5 = 0.5*abs(x2+x1),0.5*abs(y2+y1)
				angle.append(detect_angle(x,y,x5,y5))
			except:
					pass
		
		for i,j in zip(Detected_ArUco_markers.keys(),angle):
			ArUco_marker_angles[i] = j

		return ArUco_marker_angles
	except:
		pass

def mark_ArUco(img,Detected_ArUco_markers,ArUco_marker_angles):
	gray = (125,125,125)
	green = (0,255,0)
	pink = (180,105,255)
	white = (255,255,255)
	red = (0,0,255)
	blue = (255,0,0)
	font = cv2.FONT_HERSHEY_SIMPLEX
	clrs = [gray,green,pink,white]
	for p,q in zip(Detected_ArUco_markers.keys(),ArUco_marker_angles.values()):
		c_index = 0
		x1 = Detected_ArUco_markers[p][0][0]
		y1 = Detected_ArUco_markers[p][0][1]

		x2 = Detected_ArUco_markers[p][1][0]
		y2 = Detected_ArUco_markers[p][1][1]

		x3 = Detected_ArUco_markers[p][2][0]
		y3 = Detected_ArUco_markers[p][2][1]

		x4 = Detected_ArUco_markers[p][3][0]
		y4 = Detected_ArUco_markers[p][3][1]

		x, y = 0.5*abs(x3+x1),0.5*abs(y3+y1)
		x5, y5 = 0.5*abs(x2+x1),0.5*abs(y2+y1)
		img = cv2.circle(img,(int(x),int(y)),4,red,-1)
		img = cv2.line(img,(int(x),int(y)),(int(x5),int(y5)),blue,3)
		cv2.putText(img,str(q),(int(x-70),int(y)),font,1,green,2)
		cv2.putText(img,str(p),(int(x+30),int(y)),font,1,red,2)
		for q in Detected_ArUco_markers.keys():
			c_index = 0
			for i in range(0,4):
				a = Detected_ArUco_markers[q][i][0]
				b = Detected_ArUco_markers[q][i][1]
				img = cv2.circle(img,(a,b),4,clrs[c_index],-1)
				c_index = c_index + 1

	return img
