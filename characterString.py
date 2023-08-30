# 字符串
# 单引号
nameSingle = 'Tom'
print(type(nameSingle))
# 双引号
nameDouble = "Sakura"
print(type(nameDouble))
# 三引号 支持换行
nameThree = '''Tomas'''
print(type(nameThree))
nameSix = """Arthur 
is me."""
print(type(nameSix))

print(nameSingle)
print(nameDouble)
print(nameThree)
print(nameSix)

print('Hello World')
# % 格式化输出
print('My name is %s' % nameSingle)
# f表达式输出
print(f'My name is {nameSix}')

# 字符串输入
password = input('Please enter your password.\n')  # input 接收的数据，数据类型是str字符串
print('Your password is %s.' % password)

# 下标
print(nameSingle[0])

# 切片
"""
序列[开始位置下标：结束位置下标：步长] 左闭右开
"""
print(nameDouble[0:5:2])
print(nameDouble[0:5])      # default 步长 为 1， default 从0开始选取， default 选取到最后， 什么都不写选取所有
print(nameDouble[::-1])     # 步长为负数取则输出为倒叙
print(nameDouble[-5:-1])    # 下标取负数表示倒着数，从-1开始
# 如果选取方向 和 步长的方向冲突 则 无法选取数据

# 常用操作方法
# find()： 检测某个字串是否包含在字符串中，存在返回子串开始的下标，否则返回-1
# 三个参数： 子串， 查找开始位置， 查找结束位置
# 字符串.find(子串，查找的开始位置， 查找的结束位置)
helloStr = 'Hello Orlando, keep going!'
print(helloStr.find('Orlando'))

# index() 返回子串开始的下标，子串不存在报错
print(helloStr.index('Orlando'))

# count() 返回子串出现的次数
# 三个参数： 子串， 查找开始位置， 查找结束位置
print(helloStr.count('Orlando'))

# rfind() ： 与find()一致，只是从右侧开始查找,但下标都是从左侧开始计算
print(helloStr.rfind('Orlando'))

# rindex() : 与index()一致，只是从右侧开始查找，但下标都是从左侧开始计算
print(helloStr.rindex('Orlando'))

# 修改，字符串是不可变类型
# replace(): 返回修改后的字符串，不会改变原有字符串，
# 字符串.replace(旧字符串，新字符串， 替换次数) 替换次数默认为全部替换
print(helloStr.replace('Orlando', 'Rebeca', 1))

# 分割
# split(): 根据分割字符分割字符串，并丢失分割字符，返回列表
# 字符串.split(分割字符，分割次数)
print(helloStr.split(',', 1))

# 合并列表中的字符串
# join() ： 返回合并字符串
# 连接字符.join(字符串列表)
nameList = ['Orlando', 'Rebeca', 'Sakura', 'Violet']
print(' '.join(nameList))

# capitalize() 字符串首字母大写
print(helloStr.capitalize())

# title() 所有单词首字母大写
print(helloStr.title())

# upper() 所有字符大写
print(helloStr.upper())

# lower() 所有字符小写
print(helloStr.lower())

# 删除空白字符
learnStr = '  Learning python  '

print(learnStr.lstrip())
# lstrip() 删除左侧空白字符

print(learnStr.rstrip())
# rstrip() 删除右侧空白字符

print(learnStr.strip())
# strip()  删除两侧空白字符

# 字符串对齐
# ljust(对齐字符长度， 填充字符) 左对齐
# rjust(对齐字符长度， 填充字符) 右对齐
# center(对齐字符长度， 填充字符) 居中对齐

# 判断
# 字符串.startswith(子串， 开始位置， 结束位置) 返回是否以子串开头
print(helloStr.startswith('H', 0, 3))

# 字符串.endswith(子串， 开始位置， 结束位置) 返回是否以子串结尾
print(helloStr.endswith('!', 2, 5))

# isalpha() 判断是否字符串都是字母
print(helloStr.isalpha())

# isdigit() 判断是否字符串都是数字
print(helloStr.isdigit())

# isalnum() 判断是否字符串都是字母和数字组合
print(helloStr.isalnum())

# isspace() 判断是否字符串都是空格
print(helloStr.isspace())
