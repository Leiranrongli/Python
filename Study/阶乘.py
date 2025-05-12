num = input("请输入一个数字：")
num = int(num)
def kitchening(n):
    if n == 1:
        return 1
    else:
        return n * kitchening(n - 1)

print(f"{num}的阶乘为："+str(kitchening(num)))