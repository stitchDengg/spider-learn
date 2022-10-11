# _*_ coding : utf-8 _*_
# @Time : 2022/10/8 18:21
# @Author : 邓浩
# @File : 0.爬取图片
# @Project : 爬虫
# 爬取糗图百科中糗图模块中所有的图片
import requests

url = 'https://img1.baidu.com/it/u=2006656251,3871791640&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=375'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
# content返回的是二进制形式的图片数据
# text返回的是字符串形式 json返回的是字典形式的数据
img_data = requests.get(url=url,headers=headers).content

with open('./baiduImage.jpg','wb') as fp:
    fp.write(img_data)

print('over!!!')
