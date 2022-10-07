# _*_ coding : utf-8 _*_
# @Time : 2022/10/6 21:54
# @Author : 邓浩
# @File : 02_爬虫_urllib_一个类型和六个方法
# @Project : 爬虫
import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse的类型
print(type(response))

# 按照一个字节一个字节的读
# content = response.read()
#
# print(content)

# 返回5个字节
# content = response.read(5)
# print(content)

# 只能读取一行
# content = response.readline()
# print(content)

# 一行一行的读取所有
# content = response.readlines()
# print(content)

# 返回状态码 如果是200 说明没有错
print(response.getcode())

# 返回url地址
print(response.geturl())


# 返回响应头
print(response.getheaders())

# 一个类型 HTTPResponse
#   六个方法  read readline readlines getcode geturl getheaders
