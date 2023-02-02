import urllib.request

url='https://www.baidu.com'

#url的组成
#http/https协议  www.baidu.com主机  80/443端口号 s路径  wd=周杰伦：参数 #锚点

# response=urllib.request.urlopen(url)
# content=response.read().decode('utf-8')
# print(content)
#用户代理
header={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
#因为urlopen方法中不能存储字典，所以headers不能传递进去
#请求对象的定制
#因为参数位置的问题，不能直接写url和header 中间还有data，所以我们需要关键字传参
# request=urllib.request.Request(url=url,headers=header)
request=urllib.request.Request(url,{},header)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
