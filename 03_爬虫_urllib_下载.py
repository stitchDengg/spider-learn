# _*_ coding : utf-8 _*_
# @Time : 2022/10/6 22:22
# @Author : 邓浩
# @File : 03_爬虫_urllib_下载
# @Project : 爬虫
import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'
# 在python中可以直接写变量的名字 也可以直接写值
# url代表的是下载的路径
# urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片
url_img = 'https://baike.baidu.com/pic/LiSA/5001180/1/aa18972bd40735fae6cd10d7c01818b30f2442a7a20e?fr=lemma&fromModule=lemma_top-image&ct=single'
urllib.request.urlretrieve(url_img,'lisa.jpg')