# _*_ coding : utf-8 _*_
# @Time : 2022/10/8 19:06
# @Author : 邓浩
# @File : 1.正则解析
# @Project : 爬虫
import re

import requests
import os
# 创建一个文件夹 用来保存所有的图片
if not os.path.exists('./图片'):
    os.makedirs('./图片')
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8485880135978382076&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word=搞笑囧图&queryWord=搞笑囧图&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e0000000000001e&1665230412309='
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
# 使用通用爬虫对一整张页面进行爬取
img_json = requests.get(url=url,headers=headers).json()
count = 1
for imgUrlList in img_json['data']:
    # 拿json的列表
    # 遍历imgUrl
    imgData = requests.get(url=imgUrlList['thumbURL'],headers=headers).content
    count += 1
    name =str(count) + '.jpg'
    with open('./图片/' + name,'wb') as fp:
        fp.write(imgData)
        print(name,'下载成功')

# 使用聚焦爬虫对页面中所有的进行解析和提取
# ex = '<img src="(.*?)" class="photo-result-image"'
# img_src_list = re.findall(ex,page_text,re.S)
# print(img_src_list)
