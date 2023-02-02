import  urllib.request
#使用urllib来获取百度页面的源码

#定义一个url --你要访问呢的网址
url = 'http://www.baidu.com'

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen((url))


#获取相应页面的源码，read方法返回的是二进制数据 要通过decode('编码的格式')
content = response.read().decode('utf-8')

print(content)