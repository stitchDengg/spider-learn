# _*_ coding : utf-8 _*_
# @Time : 2022/10/7 16:08
# @Author : 邓浩
# @File : 05.作业肯德基餐厅位置爬取
# @Project : 爬虫
import json

import requests
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
data = {
  'cname':'',
  'pid':'',
  'keyword': '北京',
  'pageIndex': '1',
  'pageSize': '10',
}
response = requests.post(url=url,data=data,headers=headers)

text = response.json()

with open('./kfc位置.json','w',encoding='utf-8') as fp:
    json.dump(text,fp=fp,ensure_ascii=False)

print('over')