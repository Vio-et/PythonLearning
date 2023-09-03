# 公共操作
# 运算符
# + 合并 字符串、列表、元组支持
firstNameStr = 'Orlando '
lastNameStr = 'Kong'
print(firstNameStr+lastNameStr)

# * 复制 字符串、列表、元组支持
nameStr = firstNameStr + lastNameStr
print(nameStr * 2)

helloList = ['hello']
print(helloList * 3)

worldTuple = ('world', )
print(worldTuple * 4)

# in 元素是否存在 字符串、列表、元组、字典支持
# not in 元素是否不存在
partnerDict = {'Name': 'Violet'}

print('o' in firstNameStr)
print('o' not in lastNameStr)

print('hello' in helloList)
print('world' not in worldTuple)

print('Name' in partnerDict.keys())
print('Violet' in partnerDict.values())

# 公共方法
# len()
print(len(firstNameStr))
print(len(helloList))
print(len(worldTuple))
print(len(partnerDict))

# del / del()
del lastNameStr
# print(lastNameStr)

# max() min()
print(max(firstNameStr))
print(min(helloList))

# range(start, end, step) 左闭右开
for i in range(1, 10):
    print(i)

# enumerate(可遍历对象， start)  return 元组， 下标：数据
alphaList = ['a', 'b', 'c', 'd']
for i in enumerate(alphaList, start=1):
    print(i)

# 容器类型转换
# tuple()
numSet = {100, 200, 300, 400}
print(tuple(helloList))
print(tuple(numSet))

# list()
print(list(worldTuple))
print(list(numSet))

# set()
print(set(helloList))
print(set(worldTuple))
