# _*_ coding : utf-8 _*_
# @Time : 2022/10/7 15:02
# @Author : 邓浩
# @File : 03.实战之破解百度翻译
# @Project : 爬虫
import json
import requests
# 1.指定url
url = 'https://fanyi.baidu.com/sug'
# 2.ua伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
# 3.post请求参数的处理
text = input('请输入')
data = {
    'kw':text
}
# 4. 请求发送url = 'https://fanyi.baidu.com/sug'
response = requests.post(url=url,headers=headers,data=data)

# 5.获取相应数据：json方法返回的是一个obj(如果确认相应类型是json的才可以使用json)
dic_obj = response.json()

print(dic_obj)

# 6.进行持久化存储
address = f'./{text}.json'
fp = open(address,'w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)

print('over!!!!S')

