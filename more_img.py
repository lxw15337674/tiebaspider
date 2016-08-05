#多进程+多线程: 每个进程对应一个网页的爬取,每个线程对应一个网页的一张图片的下载
import threading
from multiprocessing import Pool
import time
from bs4 import BeautifulSoup
import urllib.request
import os
import random

global page_all
page_all = 1  # 每个网页图片张数


def imgdownding(img, page):
    img_name = '%s_%s.jpg' % (page, random.random())  # 设置图片名
    img_src = img['src']  # 获取图片地址
    urllib.request.urlretrieve(img_src, img_name)  # 下载到本地
    print('在第%s页成功下载%s图片' % (page,'一张'))


def use_parser(url, page):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all('img', {"class": "BDE_Image"}):
        t = threading.Thread(target=imgdownding(img, page))
        t.start()


def create_folder():
    try:
        os.mkdir('photo')
    except:
        print('photo文件夹已建立')
    os.chdir('photo')


if __name__ == '__main__':
    start = time.time()
    create_folder()
    p = Pool(5)
    for a in range(1, 10):
        p.apply_async(use_parser, args=('http://tieba.baidu.com/p/3899257862?pn=%s' % a, a,))
    p.close()
    p.join()
    end = time.time()
    print("用时%s秒" % (round(end - start, 3)))
