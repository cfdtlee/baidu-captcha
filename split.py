import cv2
import numpy as np

def getProjectData(img):
	bimg = np.divide(img, 255)
	projectData = np.divide(np.sum(np.sum(bimg, axis = 0),axis = 1),3)
	# for i in range(0:39):
	# 	for j in range(0:99):
	return projectData

def drowProjection(projectData):
	projection=np.zeros((40,100,3), np.uint8)
	for j in range(0,100):
		for i in range(0,40):
			if i < projectData[j]:
				projection[i,j] = [255, 255, 255]
	return projection

if __name__ == '__main__':
	img = cv2.imread('22.png')
	projectData = getProjectData(img)
	projection = drowProjection(projectData)
	cv2.imshow('dd',projection)
	cv2.imwrite('./projection.png',projection)
	cv2.waitKey()
