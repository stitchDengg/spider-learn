# _*_ coding : utf-8 _*_
# @Time : 2022/10/10 18:26
# @Author : 邓浩
# @File : 4.xpath解析
# @Project : 爬虫
from lxml import etree
# 配置好了一个etree对象，且将被解析的源码加载到该对象中
# 使用lxml.etree.parse()解析html文件，
# 该方法默认使用的是“XML”解析器，所以如果碰到不规范的html文件时就会解析错误
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse('test.html',parser=parser)
# r = tree.xpath('/html/body/div/div/h1')
# r = tree.xpath('//h1')
# r = tree.xpath('//h1[@class="test"]')  # 实现属性定位
# r = tree.xpath('/html/body/div/div[1]')  #索引定位
# r = tree.xpath('//h1[@class="test"]/text()')[0] #取得文本内容
r = tree.xpath('//div[@class="image"]/@style')  # 取得属性内容
print(r)
