## 字符串

print('I love you')
print("I love you") #不区分单双引号
print("""长字符串
      这是第一行
      这是第二行
      这是第三行""") #三重引号可以换行

print() # 默认换行
print("jam's home")
print('"don\'t forget me"') #主要用来区分语句中的单\双引号,如语句中单双引号都存在，则应该使用转义字符区分有歧义的单/双引号

str1 = "I love "
str2 = "you"
str3 = str1 + str2 + '\n' # 字符串拼接
print(str3) # I love you
print(str3 * 3) # 字符串重复

