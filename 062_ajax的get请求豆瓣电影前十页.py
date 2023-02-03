# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=0&limit=20
import urllib.parse
import urllib.request
def creat_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data={
        'start':(page-1)*20,
        'limit':'20',
    }
    url = base_url+urllib.parse.urlencode(data)
    # print(url)
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    }
    request=urllib.request.Request(url,{},headers)
    return request
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content
def down_load(page,content):
    with open('douban_'+str(page)+'.json','w',encoding='utf-8')as fp:
        fp.write(content)
if __name__=='__main__':
    start_page=int(input('please input the start page:'))
    end_page=int(input('please input the end page:'))
    for i in range(start_page,end_page+1):
#        每一页都定制自己的请求对象
        request=creat_request(i)
        content=get_content(request)
        down_load(i,content)
