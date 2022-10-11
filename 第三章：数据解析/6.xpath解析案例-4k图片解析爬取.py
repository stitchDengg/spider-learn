# _*_ coding : utf-8 _*_
# @Time : 2022/10/10 20:17
# @Author : 邓浩
# @File : xpath解析案例-4k图片解析爬取
# @Project : 爬虫
from lxml import etree
import requests
import os
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
if not os.path.exists('./美女'):
    os.makedirs('./美女')

def get_pic(url):
    # 拿到目标html
    res = requests.get(url=url, headers=headers)
    res.encoding = 'utf-8'
    res = res.content
    tree = etree.HTML(res)
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')
    for li in li_list:
        url = li.xpath('./a/img/@src')[0]
        name = li.xpath('./a/img/@alt')
        pic_url = 'http://pic.netbian.com/' + url
        img_data = requests.get(url=pic_url, headers=headers).content
        with open(f'./美女/{name}.jpg', 'wb') as fn:
            fn.write(img_data)
            print(name)

url = 'http://pic.netbian.com/4kmeinv/'
get_pic(url)
for i in range(2,61):
    page_url = 'http://pic.netbian.com/4kmeinv/' + f'index_{i}.html'
    get_pic(page_url)