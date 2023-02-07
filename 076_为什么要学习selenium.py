import urllib.request
url='https://www.jd.com/'
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
print(content)
//因为你 是模拟浏览器发送的请求，你没有真正的浏览器的内核，this is why we choose selenium