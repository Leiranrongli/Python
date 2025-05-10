import requests
import os

def fetch_hero_list(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
        print('请求成功')
        return response.json()
    except Exception as e:
        print(f"获取英雄列表失败: {e}")
        return []

def save_hero_info(hero_dir, hero_name, skin_names, hero_rank):
    os.makedirs(hero_dir, exist_ok=True)
    with open(os.path.join(hero_dir, f'{hero_name}.txt'), 'w', encoding='utf-8') as f:
        f.write(f'英雄名称：{hero_name}\n')
        f.write(f'皮肤名称：{skin_names}\n')
        f.write(f'排名：{hero_rank}\n')

def save_skin_info(skin_dir, hero_name, skin_name):
    os.makedirs(skin_dir, exist_ok=True)
    with open(os.path.join(skin_dir, f'{skin_name}.txt'), 'w', encoding='utf-8') as f:
        f.write(f'皮肤名称：{skin_name}\n')
        f.write(f'英雄名称：{hero_name}\n')

def download_skin_image(img_url, img_path):
    try:
        resp = requests.get(img_url, timeout=5)
        if resp.status_code == 200:
            with open(img_path, 'wb') as f:
                f.write(resp.content)
        else:
            print(f"皮肤图片下载失败: {img_url}")
    except Exception as e:
        print(f"下载图片出错: {img_url} 错误: {e}")

def main():
    url = 'https://pvp.qq.com/web201605/js/herolist.json'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }
    base_dir = './英雄数据'
    hero_list = fetch_hero_list(url, headers)
    count = 0

    for hero in hero_list:
        hero_rank = hero['ename']
        hero_name = hero['cname']
        skin_names = hero['skin_name']
        hero_dir = os.path.join(base_dir, hero_name)
        save_hero_info(base_dir, hero_name, skin_names, hero_rank)

        skin_list = skin_names.split('|')
        for idx, skin in enumerate(skin_list, 1):
            img_url = f"https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{hero_rank}/{hero_rank}-bigskin-{idx}.jpg"
            img_path = os.path.join(hero_dir, f'{skin}.jpg')
            os.makedirs(hero_dir, exist_ok=True)
            download_skin_image(img_url, img_path)
            save_skin_info(hero_dir, hero_name, skin)
        count += 1
        print(f'英雄名称：{hero_name} 爬取成功')

    print(f'爬取数量：{count}')

if __name__ == '__main__':
    main()