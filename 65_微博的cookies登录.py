import urllib.request
# 适用的场景：数据采集的时候 需要绕过登陆 然后进入到某个页面
# 个人信息页面是utf-8  但是还报错了编码错误  因为并没有进入到个人信息页面 而是跳转到了登陆页面
# 那么登陆页面不是utf-8  所以报错

# 什么情况下访问不成功？
# 因为请求头的信息不够  所以访问不成功,加入cookies的信息就可以直接绕过登陆页面
url='https://weibo.com'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)

content=response.read().decode('utf-8','ignore')
print(content)