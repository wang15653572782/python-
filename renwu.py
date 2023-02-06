import requests
import time
# 请求头,伪装成浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
keyword = '电子秤' # 关键字
max_page = 34
i=1 # 记录图片数
for page in range(1,max_page+1):
    page = page*30
    # 网址
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='\
            +keyword+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word='\
            +keyword+'&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=wallpaper&pn='\
            +str(page)+'&rn=30&gsm=1e&1596899786625='
    # 请求响应
    response = requests.get(url=url,headers=headers)
    # 得到相应的json数据
    json = response.json()
    if json.get('data'):
        for item in json.get('data')[:30]:
            # 图片地址
            img_url = item.get('thumbURL')
            # 获取图片
            image = requests.get(url=img_url)
            # 下载图片
            with open('./电子秤图片/%d.jpg' %i,'wb') as f:
                f.write(image.content) # 图片二进制数据
            time.sleep(1) # 等待1s
            print('第%d张%s图片下载完成...'%(i,keyword))
            i+=1
print('End!')
