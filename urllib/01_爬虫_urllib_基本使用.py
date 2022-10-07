# _*_ coding : utf-8 _*_
# @Time : 2022/10/6 21:41
# @Author : 邓浩
# @File : 01_爬虫_urllib
# @Project : 爬虫

# 使用urllib来获取百度首页的源代码
import urllib.request

#（1）定义一个url
url = 'http://www.baidu.com'

# （2）模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# （3）获取相应中页面的源码
# 将二进制的数据转换为字符串 解码 decode('编码的格式')
content = response.read().decode('utf-8')


# (4)打印数据
print(content)


