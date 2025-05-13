import requests
import re
import pandas

#获取网页源码
def get_news_html(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
        print('请求成功')
        return response.text
    except Exception as e:
        print(f"获取数据失败: {e}")
        return None

#获取新闻标题
def get_news_title(news_list, news, i):
    pat_title = re.compile('<p class="title">(.*?)</p>', re.S)
    title = re.findall(pat_title, news)
    for t in title:
        news_list.append({'序号': i, '标题': t.strip()})
    print('标题爬取成功')

#保存文件到Excel
def save_news_title(news_list):
    df = pandas.DataFrame(news_list)
    df.to_excel('./新闻数据.xlsx', index=False)
    print("新闻数据excel写入成功")

def main():
    news_list = []
    for i in range(1, 6):
        url = f'https://www.cqvie.edu.cn/channel_576_03{i}.html'
        headers = {
            'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'}
        news = get_news_html(url, headers)
        get_news_title(news_list, news, i)
    save_news_title(news_list)
    #保存文件到Excel

if __name__ == '__main__':
    main()