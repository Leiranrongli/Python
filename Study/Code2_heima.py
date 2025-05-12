import requests
for page in range(1,11):
    url = f'https://bbs.itheima.com/forum-425-{page}.html'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
    response = requests.get(url = url,headers = headers)
    with open(f'./heima/第{page}页.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    print('写入完成')