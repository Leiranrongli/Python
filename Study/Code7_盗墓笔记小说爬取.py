import requests
import re

#获取网页源码
def get_novel_html(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
        print('请求成功')
        return response.text
    except Exception as e:
        print(f"获取数据失败: {e}")
        return None

#获取小说内容
def get_novel_text(novel,  novel_list):
    pat_div = re.compile('<div id="nr1">(.*?)</div>', re.S)
    div = re.findall(pat_div, novel)
    div = str(div)
    if div:
        pat_text = re.compile('<p>(.*?)</p>', re.S)
        text = re.findall(pat_text, div)
        for t in text:
            novel_list.append({'小说内容': t.strip()})
        print('小说内容爬取成功')

#保存文件到txt
def save_novel_text(novel_list):

    with open('./小说数据.txt', 'w', encoding='utf-8') as f:
        for item in novel_list:
            f.write(f"{item['小说内容']}\n")
    print("小说爬取成功")

def main():
    url = 'https://www.kunnu.com/daomu/9875.htm'
    headers = {'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
    novel_list = []
    novel = get_novel_html(url, headers)
    get_novel_text(novel, novel_list)
    save_novel_text(novel_list)

if __name__ == '__main__':
    main()