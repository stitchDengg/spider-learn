# _*_ coding : utf-8 _*_
# @Time : 2022/10/11 10:49
# @Author : 邓浩
# @File : 7.xpath作业-站长简历模板爬取
# @Project : 爬虫
import requests
from lxml import etree
import os

if not os.path.exists('./简历'):
    os.makedirs('./简历')
index_url = 'https://sc.chinaz.com/jianli/zhengtao.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}


def get_tree(url):
    res = requests.get(url=url, headers=headers)
    res.encoding = 'utf-8'
    res = res.text
    tree = etree.HTML(res)
    return tree


top_tree = get_tree(index_url)
top_div_list = top_tree.xpath('//*[@id="container"]/div')
for top_div in top_div_list:
    top_url = 'https:' + top_div.xpath('./a/@href')[0]
    top_page = get_tree(top_url)
    download_url = top_page.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
    jianli_data = requests.get(url=download_url,headers=headers).content
    with open('./简历/1.rar','wb') as fp:
        fp.write(jianli_data)
