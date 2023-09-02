# 元组 不可变数据类型
# 元组的内容不可修改
numTuple = (10, 20, 30)
print(numTuple)
print(type(numTuple))

# define tuple
# 单个数据类型 必须在第一个数据之后增加 逗号,
tempTuple = (10, )
print(type(tempTuple))

# 如果没有逗号， 则整个元组变为该数据类型
tempTuple1 = (10)
print(type(tempTuple1))

# 查找
# 下标查找
print(numTuple[0])

# index() 返回下标，否则报错
print(numTuple.index(20))

# count() 返回元素在元组中出现的次数
print(numTuple.count(30))

# len() 返回元组中数据的个数
print(len(numTuple))

# 元组中的嵌套列表是可以修改的， 但不推荐
stringTuple = ('Orlando', 'Violet', ['Nanaka', 'Chisa'])
stringTuple[2][0] = 'Sakura'
print(stringTuple[2])
