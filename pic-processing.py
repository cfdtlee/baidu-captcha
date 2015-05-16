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
		if imgdir[-3:] != 'png':
			continue
		imgs.append(Image.open(dir+'/'+imgdir))
	return imgs

def saveimg(imgs):
	pwd = sys.path[0]
	i = 0
	for img in imgs:
		img.save(pwd+'/baidu/img1_after_pre/'+str(i)+'.png')
		i += 1

if __name__ == '__main__':
	pwd = sys.path[0]
	imgs = []
	imgs += getimg(pwd+'/baidu/1')
	# imgs = imgs + getimg(pwd+'/img2')
	# imgs = imgs + getimg(pwd+'/img3')
	# imgs = imgs + getimg(pwd+'/img4')
	bims = binary(imgs)
	saveimg(bims)

