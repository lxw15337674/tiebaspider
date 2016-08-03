from multiprocessing import Pool
import time
from bs4 import BeautifulSoup
import urllib.request
import os

global all
all = 0  # 总张数


def downloading(url, page):
    global all
    t = 1  # 图片张数
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all('img', {"class": "BDE_Image"}):
        img_name = '%s_%s.jpg' % (page, str(t))  # 设置图片名
        img_src = img['src']  # 获取图片地址
        urllib.request.urlretrieve(img_src, img_name)  # 下载到本地
        print('在第%s页成功下载第%s张图片' % (page, t))
        t += 1
    all += t


def create_folder():
    try:
        os.mkdir('photo')
    except:
        print('photo文件夹已建立')
    os.chdir('photo')


def main():
    start = time.time()
    create_folder()
    p = Pool(4)
    for a in range(1, 4):
        p.apply_async(downloading, args=('http://tieba.baidu.com/p/4153594193?pn=%s' % a, a,))
    p.close()
    p.join()
    end = time.time()
    print("共爬取%s张,用时%s秒" % (all, round(end - start, 3)))
