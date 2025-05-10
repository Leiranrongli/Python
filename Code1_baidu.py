import requests

#指定URL
url = 'https://www.baidu.com/'

#UA伪装
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}

#发起请求
response = requests.get(url = url,headers = headers)

#获取网页源码
#print(response.text)

#状态代码
#print(response.status_code)

#持久化存储
#with open('文件路径','w'/写,encoding = 'utf-8'/编码格式) as fp/as 别名:
with open('./baidu.html','w',encoding = 'utf-8') as fp:
    fp.write(response.text)
print('写入完成')