# # 获取url源码
# import os
# import urllib.request
# import re
#
# os.chdir('photo')
# url = "http://tieba.baidu.com/p/2166231880"
# html = urllib.request.urlopen(url).read()  # 爬取整个页面
# # reg = r'<img pic_type="0" class="BDE_Image src="(.*?.jpg)"'
# imgre = re.compile(r'<img pic_type="0" class="BDE_Image" src="(.*?.jpg)"')  # re.compile() 可以把正则表达式编译成一个正则表达式对象.
# imglist = re.findall(imgre, url)  # re.findall() 方法读取html 中包含 imgre（正则表达式）的数据


