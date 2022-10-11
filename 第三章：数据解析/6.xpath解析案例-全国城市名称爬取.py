# _*_ coding : utf-8 _*_
# @Time : 2022/10/11 09:55
# @Author : 邓浩
# @File : 6.xpath解析案例-全国城市名称爬取
# @Project : 爬虫
import requests
from lxml import etree

url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
res = requests.get(url=url, headers=headers).text
# 加载html进入etree
tree = etree.HTML(res)
div_list = tree.xpath('/html/body//div[@class="col-lg-9 col-md-8 col-sm-8 col-xs-12"]/div')
for div in div_list:
    data_lsit = div.xpath('./div')
    name = data_lsit[0].xpath('./text()')[0].strip()
    text_list = data_lsit[1].xpath('./ul/li/a/text()')
    for text in text_list:
        with open(f'./{name}.txt','a',encoding='utf-8') as fp:
            fp.write(text)
            print(f'{text}写入成功！！')


