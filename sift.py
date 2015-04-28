#coding=utf-8
import cv2
import scipy as sp

img1 = cv2.imread('/Users/eric/Desktop/12345.png',0) # queryImage
img2 = cv2.imread('/Users/eric/Desktop/1234.png',0) # trainImage

# Initiate SIFT detector
sift = cv2.SIFT()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)

print 'matches...',len(matches)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append(m)
print 'good',len(good)
# #####################################
# visualization
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]
view = sp.zeros((max(h1, h2), w1 + w2, 3), sp.uint8)
view[:h1, :w1, 0] = img1
view[:h2, w1:, 0] = img2
view[:, :, 1] = view[:, :, 0]
view[:, :, 2] = view[:, :, 0]

for m in good:
    # draw the keypoints
    # print m.queryIdx, m.trainIdx, m.distance
    color = tuple([sp.random.randint(0, 255) for _ in xrange(3)])
    #print 'kp1,kp2',kp1,kp2
    cv2.line(view, (int(kp1[m.queryIdx].pt[0]), int(kp1[m.queryIdx].pt[1])) , (int(kp2[m.trainIdx].pt[0] + w1), int(kp2[m.trainIdx].pt[1])), color)

cv2.namedWindow("view", cv2.WINDOW_NORMAL)
cv2.imshow("view", view)
cv2.waitKey()


# import cv2  
# import numpy as np  
# #import pdb  
# #pdb.set_trace()#turn on the pdb prompt  
  
# #read image  
# img = cv2.imread('./test.jpeg',cv2.IMREAD_COLOR)  
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
# cv2.imshow('origin',img);  
  
# #SIFT  
# detector = cv2.SIFT()  
# keypoints = detector.detect(gray,None)  
# img = cv2.drawKeypoints(gray,keypoints)  
# #img = cv2.drawKeypoints(gray,keypoints,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  
# cv2.imshow('test',img);  
# cv2.waitKey(0)  
# cv2.destroyAllWindows()  

