import cv2
import numpy as np
from colorSet import colorSet

def getProjectData(img):
	bimg = np.divide(img, 255)
	projectData = np.subtract(40, np.divide(np.sum(np.sum(bimg, axis = 0),axis = 1),3))
	# for i in range(0:39):
	# 	for j in range(0:99):
	return projectData

def drowProjection(projectData):
	projection=np.zeros((40,100,3), np.uint8)
	for j in range(0,100):
		for i in range(0,40):
			if i < np.subtract(40, projectData[j]):
				projection[i,j] = [255, 255, 255]
	return projection

def getSplitPosition(projectData):
	splitPosition = []
	if projectData[1] > projectData[0]:
		isUp = 1
	else:
		isUp = 0
	for i in range(1, 99):
		if isUp == 0 and projectData[i+1] > projectData[i]:
			isUp = 1
			splitPosition.append(i)
		elif isUp == 1 and projectData[i+1] < projectData[i]:
			isUp = 0
	return splitPosition


class Block():
	"""docstring for Block"""
	def __init__(self, arg):
		coordinate = []
		color = []
		start = []

def split(img, splitPosition):
	pass

if __name__ == '__main__':
	img = cv2.imread('29.png')
	projectData = getProjectData(img)
	print projectData
	projection = drowProjection(projectData)
	print getSplitPosition(projectData)
	cv2.imshow('dd',projection)
	cv2.imwrite('./projection29.png',projection)
	cv2.waitKey()

