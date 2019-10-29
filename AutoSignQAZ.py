# -*- coding: utf-8 -*-
import requests
import json
import time

username = ['user1','user2']
password = ['pass1','pass2']

def sign(i):
	header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/2008052906 Firefox/3.0'}
	url = 'https://qaz.moe/auth/login'
#设置代理
	proxy = '127.0.0.1:8118'
	proxies = {
		'http': 'http://' + proxy,
		'https': 'https://' + proxy
	}
	
#获取COOKIES
	form = {
		'email': username[i],
		'passwd': password[i],
		'code' : ''
	}
#	r = requests.post(url, form,proxies=proxies,verify = True)
	r = requests.post(url, form,verify = True,headers=header)
#	print(r.text)
	data = json.loads(r.text)
	print(data)

#签到	
	urlsign = 'https://qaz.moe/user/checkin'
#	res = requests.post(urlsign,cookies=r.cookies,proxies=proxies,verify = True)
	res = requests.post(urlsign,cookies=r.cookies,verify = True,headers=header)	
	data = json.loads(res.text)
	return data


while True:
	try:
		for i in range (len(username)):
			result = sign(i)
			print(result)
			if (result["ret"] == 1):
				print(str(i)+')> 签到成功，5小时后下一个')
			else:
				print(str(i)+')> 签到过啦，5小时后下一个')
			for j in range(5):
				localtime = time.asctime( time.localtime(time.time()) )
				print ("当前时间为 :", localtime)	
				print(str(j)+' 30min后继续')	
				time.sleep(1800)
	
	except Exception as e:	
		print('出现异常，600s后重试')
		time.sleep(600)