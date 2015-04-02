# coding = utf-8
import Image
import sys, os

table = [0 for x in range(230)]+[1 for x in range(26)]

def binary(imgs):
	bims = []
	for img in imgs:
		bims.append(img.convert('L').point(table, '1'))
	return bims

def getimg(dir):
	imgs = []
	imgdirs = os.listdir(dir)
	imgdirs = imgdirs[1:]
	for imgdir in imgdirs:
		imgs.append(Image.open(dir+'/'+imgdir))
	return imgs

def saveimg(imgs):
	pwd = sys.path[0]
	i = 1
	for img in imgs:
		img.save(pwd+'/bimg/'+str(i)+'.gif')
		i += 1

if __name__ == '__main__':
	pwd = sys.path[0]
	imgs = []
	imgs += getimg(pwd+'/img1')
	imgs = imgs + getimg(pwd+'/img2')
	imgs = imgs + getimg(pwd+'/img3')
	imgs = imgs + getimg(pwd+'/img4')
	bims = binary(imgs)
	saveimg(bims)

