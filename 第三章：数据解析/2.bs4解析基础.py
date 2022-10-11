# _*_ coding : utf-8 _*_
# @Time : 2022/10/8 20:51
# @Author : 邓浩
# @File : bs4解析基础
# @Project : 爬虫
from bs4 import BeautifulSoup
# 将本地的html文档的数据加载中到该对象中
fp = open('./test.html',encoding='utf-8')
soup = BeautifulSoup(fp,'lxml')
# print(type(soup)) # <class 'bs4.BeautifulSoup'>
# print(soup.div)  #soup.tagName 返回的是html中第一次出现的tagName标签
# soup.find('tagName)等同于soup.div
# print(soup.find('div'))   # print(soup.div)
# print(soup.find('div',class_='text'))
# print(soup.find_all('div'))  # 找到所有的div标签
# print(soup.select('.heading')[0].get_text()) # 通过选择器得到节点对象 > 表示的是一个层级
print(soup.select('.image')[0]['style'])







