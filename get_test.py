import requests
#url="http://www.baidu.com?id=1001"
#url="http://www.baidu.com"
#params={"id":"1001,1002"}
# params={"id":"1001","kw":"北京"}
# data={"aa":"1002"}
# header={"content-Type":"application/json"}
# response=requests.get(url,params)
# print(response.url)
# print(response.status_code)
# print(response.encoding)
# response.encoding="utf-8"
#
# #r=requests.post(url,json=data,headers=header)
# #print(r.json())
# #print(response.text)
# print(response.cookies)
# print(response.cookies["BDORZ"])
picurl='http://wx.tp-shop.cn/client/user/verify?type=user_login&t=0.7524376960649903'
url="http://wx.tp-shop.cn/client/user/login"
code="GTUC"
data={"username":"13410559632",
"password":"123456",
"verify_code":"2mvk"}
# r1=requests.get(picurl)
# cookies1=r1.cookies["PHPSESSID"]
# cookies={"PHPSESSID":"mg80bn3ui9nvfbe0jbqf3lhek2"}
# print("cookies",cookies)
#
# r=requests.post(url,data=data,cookies=cookies)
session=requests.session()
session.get(picurl)
r=session.post(url,data=data)
print(r.status_code)
print(r.json())
