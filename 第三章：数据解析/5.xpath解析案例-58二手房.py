# _*_ coding : utf-8 _*_
# @Time : 2022/10/10 19:47
# @Author : 邓浩
# @File : 5.xpath解析案例-58二手房
# @Project : 爬虫
# 需求：爬取58二手房相关的房源信息
import requests
from lxml import etree
url = 'https://bj.58.com/ershoufang/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
# 拿到页面html
res = requests.get(url=url,headers=headers).text
# xpath加载网页
tree = etree.HTML(res)
p = tree.xpath('//h3[@class="property-content-title-name"]')
print(p)