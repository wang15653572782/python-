
# urllib
# (1) 一个类型以及六个方法
# （2）get请求
# （3）post请求   百度翻译
# （4）ajax的get请求
# （5）ajax的post请求
# （6）cookie登陆 微博
# （7）代理


# requests
# (1)一个类型以及六个属性
# （2）get请求
# （3）post请求
# （4）代理
# （5）cookie  验证码


import requests

url = 'https://www.baidu.com/s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
'Cookie': 'BAIDUID=BF0E23EE080569D1A02109D1AB324B68:FG=1; BDUSS=TZxc2oza05xclI2a05FM0VGazBUVHlmTWNHZUZrdWU4OVVLOU1JZmhBV0ZjdHhqSVFBQUFBJCQAAAAAAQAAAAEAAADAiwEfzfWzrLeyMjAwMjA1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIXltGOF5bRjU; BDUSS_BFESS=TZxc2oza05xclI2a05FM0VGazBUVHlmTWNHZUZrdWU4OVVLOU1JZmhBV0ZjdHhqSVFBQUFBJCQAAAAAAQAAAAEAAADAiwEfzfWzrLeyMjAwMjA1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIXltGOF5bRjU; BIDUPSID=BF0E23EE080569D1A02109D1AB324B68; PSTM=1674570074; BD_UPN=12314753; BAIDUID_BFESS=BF0E23EE080569D1A02109D1AB324B68:FG=1; baikeVisitId=137e99aa-9250-41b5-86b1-c0d2f22d47fa; ZFY=:A2Xwin1ifbM:BvYAVcR0:AqRoy0b5A:AC4NB7:BhXvz7xXc:C; B64_BOT=1; BD_HOME=1; H_PS_PSSID=36546_37517_38093_38128_37910_37989_37799_37922_38088_26350_38008_37881; BA_HECTOR=8g0480ag0584a42l85aka0tj1hu4d711k'


   }

data = {
    'wd':'北京'
}


# url  请求资源路径
# params 参数
# kwargs 字典
response = requests.get(url=url,params=data,headers=headers)

content = response.text

print(content)

# 总结：
# （1）参数使用params传递
# （2）参数无需urlencode编码
# （3）不需要请求对象的定制
# （4）请求资源路径中的？可以加也可以不加