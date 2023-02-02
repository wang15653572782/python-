#https://www.baidu.com/s?tn=68018901_2_oem_dg&ie=utf-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
#需求 获取https://www.baidu.com/s?tn=68018901_2_oem_dg&ie=utf-8&wd=周杰伦的网页源码
import urllib.request
import urllib.parse
url='https://www.baidu.com/s?tn=68018901_2_oem_dg&ie=utf-8&wd='

name=urllib.parse.quote('周杰伦')
url=url+name
#请求对象的定制是解决反爬的第一种手段
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

#请求对象的定制
request=urllib.request.Request(url,{},headers)



#模拟浏览器向服务器发送请求

response=urllib.request.urlopen(request)


print(response.read().decode('utf-8'))