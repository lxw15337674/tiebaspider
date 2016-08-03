# 此为多进程爬虫,不能计算下载图片的总张数,因为没有解决进程间的通信
# 此状态下global all不能使用,因为global并不能在方法使用,必须在方法中再次global,当多个进程同步进行,获取的全局变量all均为0
# 而声明list可以是真正的全局变量,而不需要再声明

from multiprocessing import Pool
import time
from bs4 import BeautifulSoup
import urllib.request
import os


def downloading(url, page):
    t = 1  # 图片张数
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all('img', {"class": "BDE_Image"}):
        img_name = '%s_%s.jpg' % (page, str(t))  # 设置图片名
        img_src = img['src']  # 获取图片地址
        urllib.request.urlretrieve(img_src, img_name)  # 下载到本地
        print('在第%s页成功下载第%s张图片' % (page, t))
        t += 1
    list.append(t)


def create_folder():
    try:
        os.mkdir('photo')
    except:
        print('photo文件夹已建立')
    os.chdir('photo')


if __name__ == '__main__':
    start = time.time()
    create_folder()
    p = Pool(4)
    for a in range(1, 5):
        p.apply_async(downloading, args=('http://tieba.baidu.com/p/4153594193?pn=%s' % a, a,))
    p.close()
    p.join()
    end = time.time()
    print("用时%s秒" % ( round(end - start, 3)))
