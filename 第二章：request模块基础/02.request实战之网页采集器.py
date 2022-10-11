# _*_ coding : utf-8 _*_
# @Time : 2022/10/7 14:32
# @Author : 邓浩
# @File : 02.request实战之网页采集器
# @Project : 爬虫
import requests
# UA伪装 :门户网站的服务器会检测对应请求头的载体身份标识，如果检测到的请求载体身份标识为
# 某一款浏览器，就说明请求是一个正常的请求，如果请求的标识不是浏览器的就一定不是正常的请求
# UA user-agent
# 将对应的user-agent封装到字典中
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
url = 'https://www.sogou.com/web'
# 处理url携带的参数:封装到字典中
kw = input('enter a word')
param = {
    'query':kw
}

# 对指定的url发送了请求是携带了参数的，并且请求过程中已经处理了参数
response = requests.get(url = url,params = param,headers = headers)

page_text = response.text
filename = kw + '.html'
with open(filename,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(filename,'保存成功！！')
