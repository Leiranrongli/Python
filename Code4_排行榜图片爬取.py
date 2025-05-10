import requests
import os
import pandas

url = 'https://movie.douban.com/j/chart/top_list'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}

para = {'type':'16','interval_id':'100:90','action':None,'start':'0','limit':'20'}
response = requests.get(url = url,headers = headers,params=para,timeout=3)

data = response.json()
print(data)
movie_list = []
# 遍历电影数据
for t in data:
    movieRank = t["rank"]
    movieName = t["title"]
    movieDate = t["release_date"]
    movieScore = t["score"]
    movieRegions = t["regions"]
    movieTypes = t["types"]
    movieActors = t["actors"]
# 将数据添加到列表中
    movie_list.append({
        "排名" : movieRank,
        "电影名称": movieName,
        "发布日期":movieDate,
        "评分": movieScore,
        "地区": ", ".join(movieRegions),
        "类型": ", ".join(movieTypes),
        "演员":",".join(movieActors)
    })
    # 创建电影数据文件夹
    os.makedirs('./电影数据',exist_ok=True)
    # 写入电影数据到txt文件
    with open( f'./电影数据/{movieName}.txt','w',encoding='utf-8') as Movie:
        Movie.write(f'电影名称：{movieName}\n')
        Movie.write(f'排名：{movieRank}\n')
        Movie.write(f'发布日期：{movieDate}\n')
        Movie.write(f'评分：{movieScore}\n')
        Movie.write(f'地区：{", ".join(movieRegions)}\n')
        Movie.write(f'类型：{", ".join(movieTypes)}\n')
        Movie.write(f'演员：{",".join(movieActors)}\n')
    print(f'电影名称：{movieName} 爬取成功')
# 将数据添加到excel文件中
df = pandas.DataFrame(movie_list)
df.to_excel('./电影数据/电影.xlsx', index=False)
print('电影数据excel写入成功')
