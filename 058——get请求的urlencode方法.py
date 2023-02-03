#引用场景：多个参数的时候

#https://www.baidu.com/s?wd=周杰伦&sex=男
import urllib.parse
import  urllib.request
data={
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}
base_url='https://www.baidu.com/s?tn=68018901_2_oem_dg&ie=utf-8&'
a=urllib.parse.urlencode(data)
url=base_url+a
#print(url)
# print(a)
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
request=urllib.request.Request(url,{},headers)
da=urllib.request.urlopen(request)
content=da.read().decode('utf-8')
print(content)