import requests

url = 'https://img2.doubanio.com/view/photo/l/public/p2916323291.webp'

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}

response = requests.get(url = url,headers = headers,timeout = 3)

with open('./哪吒.jpg','wb') as fp:
    fp.write(response.content)
print('图片保存完成')
