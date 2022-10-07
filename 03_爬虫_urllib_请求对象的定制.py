# _*_ coding : utf-8 _*_
# @Time : 2022/10/6 22:34
# @Author : 邓浩
# @File : 03_爬虫_urllib_请求对象的定制
# @Project : 爬虫
import urllib.request

url = 'https://www.baidu.com'

response = urllib.request.urlopen(url)

content = response.open()