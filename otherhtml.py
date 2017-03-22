# 此为单线程的爬虫,作用:对贴吧中一个帖子中所有图片爬取,其中页数需手动输入,需要解决
import time
from bs4 import BeautifulSoup
import urllib.request
import os


def downloading(url, page):
    t = 1  # 图片张数
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
	#<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=1a2334a804087bf47dec57e1c2d2575e/f91c501ed21b0ef41c6393bddbc451da83cb3ea3.jpg" changedsize="true" width="560" height="316" size="25748" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;">
    for img in soup.find_all('img', {"class": "BDE_Image"}):
        img_name = '%s_%s.jpg' % (page, str(t))  # 设置图片名
        img_src = img['src']  # 获取图片地址
        urllib.request.urlretrieve(img_src, img_name)  # 下载到本地
        print('在第%s页成功下载第%s张图片' % (page, t))
        t += 1
    return t


if __name__ == '__main__':
    start = time.time()
    try:
        os.mkdir('photo')
    except:
        print('photo文件夹已建立')
    os.chdir('photo')
    all = 0  # 总张数
    for a in range(1, 4):
        all += downloading('http://tieba.baidu.com/p/4153594193?pn=%s' % a, a)
    end = time.time()
    print("共爬取%s张,用时%s秒" % (all, round(end - start, 3)))

	<div class="entry-content">
<p><img class="aligncenter" src="http://ww2.sinaimg.cn/large/006pqlgDgw1f7ps7mothqj30rl13y0xd.jpg" alt="" width="459" height="664"><br>
中年教师猥琐大叔征服初中软妹的故事，其男友被各种花式NTR却被蒙在鼓里，最终连其母亲也被攻略下来，真是可喜可贺 ╮(╯▽╰)╭<br>
<a href="https://blog.reimu.net/archives/12413#more-12413" class="more-link">继续阅读<span class="screen-reader-text">【R0397】[ひとのふんどし (ゆきよし真水)] 夏期補習 1-7 汉化合集</span></a></p>
</div>