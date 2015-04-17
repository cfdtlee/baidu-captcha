# coding = utf-8
import Image
import sys, os
from copy import deepcopy

# up, down, left, right, (90*40)
# regpos=(0, 0, 0, 0,)

def findreg(img):
	if img.getpixel((0, 0)) == 0: # black: 0, white: 255
		down = 1
		while img.getpixel((0, down)) == 0:
			down += 1
			if down >= 40:
				break
			print 'down = ', down
		return (0, down, 0, 100)
	elif img.getpixel((0,39)) == 0:
		up = 38
		while img.getpixel((up, 0)) == 0:
			up -= 1
			if up <= 0:
				break
		return (up, 40, 0, 100)
	else:
		# find up bound
		maxcount = 0
		row_maxcount = [0 for x in range(0,19)]
		upbound = (0, 0, 0, 0,) #(upx1, upy1, upx2, upy2)
		#get a list of maxcount of each row: row_maxcount
		for y in range(1, 19):
			count = 0
			for x in range(0, 99): # find longest edge of each line
				# begin = 0
				# row_maxcount = 0
				# row_maxbound = (0, 0, 0, 0,)
				if img.getpixel((x,y)) != img.getpixel((x, y-1)):
					count += 1
				else:
					if count > row_maxcount[y]:
						row_maxcount[y] = count
						# row_maxbound = (begin, y, x-1, y,)
					count = 0
		up = row_maxcount.index(max(row_maxcount))
		# print up
		# find the begin and end of the edge
		begin = 0
		count = 0
		for x in range(0, 99):
			if img.getpixel((x, up)) != img.getpixel((x, up-1)):
				count += 1
				if count == max(row_maxcount):
					end = x + 1
					break
			else:
				begin = x + 1
				count = 0
		upbound = (begin, up, end, up)
		
		# find lower bound
		maxcount = 0
		row_maxcount = [0 for x in range(0,19)]
		downbound = (0, 0, 0, 0,) #(downx1, downy1, downx2, downy2)
		#get a list of maxcount of each row: row_maxcount
		for y in range(21, 39):
			count = 0
			for x in range(0, 99): # find longest edge of each line
				if img.getpixel((x,y)) != img.getpixel((x, y-1)):
					count += 1
				else:
					if count > row_maxcount[y-20]:
						row_maxcount[y-20] = count
						# row_maxbound = (begin, y, x-1, y,)
					count = 0
		down = row_maxcount.index(max(row_maxcount))+20
		# find the begin and end of the edge
		print max(row_maxcount)
		begin = 0
		count = 0
		for x in range(0, 99):
			if img.getpixel((x, down)) != img.getpixel((x, down-1)):
				count += 1
				if count == max(row_maxcount):
					end = x + 1
					break
			else:
				begin = x + 1
				count = 0
		downbound = (begin, down, end, down)
		print upbound, downbound

		if upbound[2] - upbound[0] == 50:
			left = upbound[0]
			right = upbound[2]
		elif downbound[2] -downbound[0] ==50:
			left = downbound[0]
			right = downbound[2]
		elif upbound[2] - downbound[0] ==50:
			left = downbound[0]
			right = upbound[2]
		elif downbound[2] - upbound[0] == 50:
			left = upbound[0]
		 	right = downbound[2]
		else:
			#find left and right bound
			l = downbound[0]
			if upbound[0] < downbound[0]:
				l = upbound[0]
			r = downbound[2]
			if upbound[2] > downbound[2]:
				r = upbound[2]
			col_maxcount=[0 for x in range(0, 100)]
			# print l, r   ---ok
			for x in range(1, 100):
				count = 0
				for y in range(0, 39):
					if img.getpixel((x,y)) != img.getpixel((x-1, y)):
						count += 1
					else:
						if count > col_maxcount[x]:
							col_maxcount[x] = count
							# row_maxbound = (begin, y, x-1, y,)
						count = 0
			col_maxcount_sort = deepcopy(col_maxcount)
			col_maxcount_sort.sort(reverse = True)
			i1 = col_maxcount.index(col_maxcount_sort[0])
			print col_maxcount
			col_maxcount.remove(col_maxcount_sort[0])
			print col_maxcount
			i2 = col_maxcount.index(col_maxcount_sort[1])
			if i2 > i1:
				i2 += 1
			print i1, i2
			if i1 < i2:
				left = i1
				right = i2
			else:
				left = i2
				right = i1
		return (up, down, left, right)


def revert(img, regpos):
	(up, down, left, right) = regpos
	for x in range(left, right):
		for y in range(up, down):
			if img.getpixel((x, y)) == 0:
				img.putpixel((x, y), 255)
			else:
				img.putpixel((x, y), 0)
	return img

if __name__ == '__main__':
	pwd = sys.path[0]
	img_urls = os.listdir(pwd + '/img1_binary')
	for img_url in img_urls:
		print 'img_url:' + img_url
		img = Image.open('./img1_binary/' + img_url)
		regpos = findreg(img)
		img_r = revert(img, regpos)
		img_r.save('./img1_after_pre/' + img_url, 'gif')
	
	# img = Image.open('./11.gif')
	# regpos = findreg(img)
	# print regpos
	# img_r = revert(img, regpos)
	# img_r.show()
