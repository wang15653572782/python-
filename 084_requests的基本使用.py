import requests
url='http://www.baidu.com'

response=requests.get(url)

# print(type(response))
#一个类型和六个属性
#Response类型
#设置响应的编码格式
# response.encoding='utf-8'
# #以字符串的形式来返回了网页的源码
# print(response.text)
# #return a url address
# print(response.url)

#返回的是二进制的数据
# print(response.content)

#返回响应的状态码
# print(response.status_code)

#返回的是响应头
# print(response.headers)
