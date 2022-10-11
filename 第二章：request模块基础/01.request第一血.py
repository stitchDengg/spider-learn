# _*_ coding : utf-8 _*_
# @Time : 2022/10/7 13:55
# @Author : 邓浩
# @File : 01.request第一血
# @Project : 爬虫

# 爬取搜狗首页页面数据
import requests

# step 1:指定url
url = 'https://www.sogou.com/'

# step 2:发送请求
# get方法会返回一个相应对象
response = requests.get(url)

# step 3:获取相应数据,text返回的是字符串形式的响应数据
page_text = response.text
print(page_text)

# step 4:持久化存储
with open('./sougo.html','w',encoding='utf-8') as fp:
    fp.write(page_text)

print('爬取数据结束！')
