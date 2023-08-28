# @Orlando Hello World

print("Hello World")

# 输出print函数
age = 18
name = 'Orlando'
weight = 69.5
studentID = 150
print("My age is %d." % age)
print("My name is %s." % name)
print("My weight is %.2f" % weight)
print("My student ID is %03u" % studentID)
print("My name is %s and my age is %d" % (name, age))
print("My name is %s and my age is %d, my weight is %.2f, my student ID is %03u" % (name, age, weight, studentID))

# %s 可以输出任何语句
print("My name is %s and my age is %s, my weight is %s, my student ID is %s" % (name, age, weight, studentID))

# f'{表达式}' 格式化字符串
print(f'My name is {name} and my age is {age}')

# 转义字符
print('Hello\nPython')
print('\tABCD')

# 默认print结束符为换行符
print('Hello')
print('Python', end="\t")
print('World')
