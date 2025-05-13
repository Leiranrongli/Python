import requests
import pandas

def save_ranking_info(base_dir, idx, title, bv, video_partition, short_link, video_list):
    with open(base_dir, 'a', encoding='utf-8') as f:
        f.write(f"排名：{idx}|")
        f.write(f"标题：{title}|")
        f.write(f"BV号：{bv}|")
        f.write(f"分区：{video_partition}|")
        f.write(f"短链接：{short_link}")
        f.write("\n")
    video_list.append({
        "排名": idx,
        "标题": title,
        "BV号": bv,
        "分区": video_partition,
        "短链接": short_link
    })

def get_bilibili_ranking(url, headers, params):
    try:
        response = requests.get(url, headers=headers, params=params, timeout=3)
        response.raise_for_status()  # 检查请求是否成功
        print("请求成功")
        return response.json()
    except Exception as e:
        print(f"获取数据失败: {e}")
        return None

def main():
    url = 'https://api.bilibili.com/x/web-interface/ranking/v2'
    headers = {
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
    params = {'rid': '0', 'type': 'all'}
    ranking_list = get_bilibili_ranking(url, headers , params)
    base_dir = 'bilibili_ranking_info.txt'
    count = 0
    video_list = []

    for idx, video in enumerate(ranking_list['data']['list'],1):
        title = video['title']
        bv = video['bvid']
        video_partition = video['tname']
        short_link = video['short_link_v2']
        save_ranking_info(base_dir,idx, title, bv, video_partition, short_link, video_list)
        count += 1
    print("视频爬取完成")

    df = pandas.DataFrame(video_list)
    df.to_excel('./bilibili_ranking.xlsx', index=False)
    print("视频数据excel写入成功")

if __name__== '__main__':
    main()