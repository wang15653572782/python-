import urllib.request

url='http://www.baidu.com/s?tn=68018901_2_oem_dg&ie=utf-8&wd=ip'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}
request=urllib.request.Request(url,{},headers)

# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)

proxies = {
    'http':'117.78.6.150'
}
# handler  build_opener  open
handler = urllib.request.ProxyHandler(proxies = proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应的信息
content = response.read().decode('utf-8')

# 保存
with open('daili1.html','w',encoding='utf-8')as fp:
    fp.write(content)
