# coding:utf-8
"""
some function by metaphy,2007-04-03,copyleft
version 0.2
"""
import urllib, httplib, urlparse, urllib2
from urllib import urlopen
import re
import random
import thread
import time 

def gDownloadWithFilename(url,savePath,file):
	#参数检查，现忽略
	try:
		urlopen=urllib.URLopener()
		fp = urlopen.open(url)
		data = fp.read()
		fp.close()
		file=open(savePath + file,'w+b')
		file.write(data)
		file.close()
	except IOError:
		print "download error!"+ url
		
def gDownload(url,savePath, n):
	#参数检查，现忽略
	# fileName = gGetFileName(url)
	#fileName =gRandFilename('jpg')
	for i in range(1,1000):
		fileName = str(i)+'.jpeg'
		gDownloadWithFilename(url,savePath+str(n)+'/',fileName)


url = 'https://passport.baidu.com/cgi-bin/genimage?captchaservice656436363363666755364e764b4f62414e6135494233635768597633586668386a2b4171334a63334d325555654b6e5241566f4f68755476337a526f51697a504e2b6a5a36333744767445645a373454634e514d7554456849574f716d4d434932424b303272575577547a51345a4d4d6f652f635653616a705654737355626176464b392f584953642b434852664d5566575a363753597731653835744e6636474159584d3332377977516637366975634e71714c4e42746d2b662f573442324a645135565272787076344f6c4878414355415a76644772323948752f736162724e686e6f4e75335465414b5a46646a716d456b454e54627a5755722f744747367332556a6e35644b446952636f59483152464a62395475716a5431785a535854354b762f784558536c6e504e4863'
# url2 salt
url2 = 'https://passport.baidu.com/cgi-bin/genimage?captchaservice62383836682b67536a736c6953524346663552653463594a395a6f4b593177424b774865375543337077734b467972597447445962697545674866746839354c61436f572f594e6148647246436377656e2b33382b47786964664e6550625a61436b4b724c583675432f6548587a7752454f6473334c346735564b6f656370515a58396757483479346a6b33774f4753777864505a583145416c6b412b317374476d48764f4b38624662594855554a623265435979694a4c7436686e4b34505a4964492b38716f302b503546676b506853726f48626a586f7878343770457458734e526c48684c666d564e74462b77436e6a2f343633576144525a5749346470475373634a7a4849486f553432307a3745715a494f78677236516a525432596a45336f2b6d396658725876324b4e3734&v=1415774034050'
# url3 quit + hallow
url3 = 'https://passport.baidu.com/cgi-bin/genimage?captchaservice303162315766505a77626e38632b706d554c345572792b31663774436f5153436f7147414533726f514e376b4a36696f6f4232482f526c4b6b4e6b4c6f41567a3647656b566c4a506361303261496b6a642b336e76537251556e3545384b493959345164393678786e544677776e4852467442585842684663353541463050695538335664515863323231537a4b6e4d38316c524f523236516f6d30774b677141384c6c394a4876514f335957585762756c334a484a306b524878576452556c76506f5a4e66313639416b32526e71554879446c5448356337427247626d7769463146786a48797447614376536f38796c372b4b5230356257393478526365726a4468646c323837326e505a70434e4d5471654563747476617868796b4263534559576a6a44387555357a34702f45'
# url4 移位
url4 = 'https://passport.baidu.com/cgi-bin/genimage?captchaservice62366164674c626b465a435653445a69344578526c6461586256637673772f50512b73372f63622f6f6c6c6f317a4f68747465336c4e364a426d52554f4858644f58533533446d785934575a7135445766436d414930775a5a7273753752326f6d6b574c4c7956357459317337365256615a4270464d796153734d75616d367a734b4f54366246685749386e495859466533314348413239665a354561346d43733266527266384350674a3762693338646939526930703843546c6632454336685566626c484f6f464b5879304e656d74433951427a4d5650416c716776716e3746536b62634171417735382b55385a6d68327153564861763162384856797a646271746d686654757154626d6541624d69376150452b6a32556c51645a7a49796139675a665663327a454d7651'

savePath = '/Users/eric/Documents/Programming/baidu-captcha/img'
# for i in range(1,31):
# 	gDownload(url4, savePath, i)
# 	print "saved"+str(i)

gDownload(url2, savePath, 2)
gDownload(url3, savePath, 3)
gDownload(url4, savePath, 4)