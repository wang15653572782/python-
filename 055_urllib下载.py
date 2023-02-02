import urllib.request

#下载网页
url_page='http://www.baidu.com'

#url代表的是下载路径，filename文件的名字
#在python中可以变量的名字，也可以直接写值
# urllib.request.urlretrieve(url_page,'baidu.html')

#下载图片
# url_image='https://th.bing.com/th/id/OIP.Ky6yzSwl91B8P3mNwidOqgHaLV?w=196&h=300&c=7&r=0&o=5&dpr=1.5&pid=1.7'
# urllib.request.urlretrieve(url=url_image,filename='idol.jpg')

#下载视频
url_video='https://vd2.bdstatic.com/mda-khcriybszxhpzqsy/v1-cae/sc/mda-khcriybszxhpzqsy.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1675345661-0-0-f73cd3864c03cfcde30ebd35df8c856a&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=1061195038&vid=8480004725184573789&abtest=106847_1&klogid=1061195038'
urllib.request.urlretrieve(url_video,'inspire.mp4')
