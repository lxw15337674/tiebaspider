# from bs4 import BeautifulSoup
import urllib.request
import os


def downloading(url):
    t = 1  # 图片张数
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all('img', {"class": "BDE_Image"}):
        img_name = str(t) + '.jpg'  # 设置图片名
        img_src = img['src']  # 获取图片地址
        urllib.request.urlretrieve(img_src, img_name)  # 下载到本地
        print('下载第%s张' % t)
        t += 1

if __name__ == '__main__':
    try:
        os.mkdir('photo')
    except:
        print('photo文件夹已建立')
    os.chdir('photo')
    downloading('http://tieba.baidu.com/p/4153594193?pn=')