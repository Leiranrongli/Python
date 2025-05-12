listA = ['I', 'love', 'you', 'I', 'love']
print(listA[-2])

for idx, item in enumerate(listA , 1):
    print(f"排名：{idx}，值：{item}")
# print(idx)
while idx > 0:
    print(listA[idx-1], end = '')
    idx -= 1
