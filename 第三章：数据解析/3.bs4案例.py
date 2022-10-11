# _*_ coding : utf-8 _*_
# @Time : 2022/10/10 17:10
# @Author : 邓浩
# @File : 3.bs4案例
# @Project : 爬虫
# 需求：爬取三国演义小说所有的章节标题和章节内容
import os
import requests
from bs4 import BeautifulSoup

if not os.path.exists('./三国演义'):
    os.makedirs('./三国演义')

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}


def getData(url):
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')
    return soup


soup = getData(url)
title_list = soup.select('.book-mulu li')
count = 1
for title in title_list:
    article_url = 'https://www.shicimingju.com/book/sanguoyanyi/' + str(count) + '.html'
    article_soup = getData(article_url)
    article_text = article_soup.select('.chapter_content')[0].get_text()
    with open(f'./三国演义/{title.get_text()}.txt', 'w') as fp:
        fp.write(article_text)
        print(f'{title.get_text()}成功写入')
