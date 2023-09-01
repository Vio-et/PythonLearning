import random
# 列表 list 可变数据类型
# list 可以存储多个数据，可以为多种数据类型

# 查找
nameList = ['Orlando', 'Rebeca', 'Lisa', 'Sakura']
print(nameList)
print(nameList[0], nameList[1])

# index()
print(nameList.index('Orlando'))

# count()
print(nameList.count('Lisa'))

# len()
print(len(nameList))

# 判断是否存在
# in
print('Rebeca' in nameList)

# not in
print('Sakura' not in nameList)

name = input('Please enter your username.\n')

if name in nameList:
    print(f'This username {name} has already existed.')
else:
    nameList.append(name)
    print('Well done.')
    print(nameList)

# 增加 列表中的元素也可以是列表
# append() : 结尾处增加数据,能增加序列
nameList.append(['Nanaka', 'Chisa'])
print(nameList)

# extend() : 结尾处增加数据,不能增加序列，将会拆分增加
nameList.extend(['Nami', 'Hancock'])
print(nameList)

# insert()
# insert(location, data)
nameList.insert(1, 'Violet')
print(nameList)

# 删除
# del 可以删除指定下标的数据
# del nameList
del nameList[3]
print(nameList)

# pop()
# pop() 默认删除最后一个数据，返回被删除的数据
delName = nameList.pop(3)
print(delName)
print(nameList)

# remove() 依据数据删除
# remove(data)
nameList.remove('Nami')
print(nameList)

# clear() 清空列表
# nameList.clear()
# print(nameList)

# 修改
# reverse() 逆序
nameList.reverse()
print(nameList)

# sort() 排序 默认为升序排序
# sort(key = None, reverse = False) 默认升序False，降序为True
numList = [1, 2, 3, 4, 0, 5, 7]
numList.sort()
print(numList)

numList.sort(reverse=True)
print(numList)

# 复制
# copy()
nameListCopy = nameList.copy()
print(nameList)
print(nameListCopy)

# list 循环遍历
# while 遍历
i = 0
while i < len(nameList):
    print(nameList[i])
    i += 1

# for 遍历
for name in nameList:
    print(name)

# 列表嵌套
monickerList = [['Orlando'], ['Nami', 'Robin', 'Hancock'], ['Nanaka', 'Chisa'], ['Sakura', 'Hinata']]
print(monickerList)

# 查询
print(monickerList[0][0])


partnerList = ['Orlando', 'Nami', 'Robin', 'Hancock', 'Nanaka', 'Chisa', 'Sakura', 'Hinata']
roomList = [[], [], []]
for partner in partnerList:
    roomList[random.randint(0, 2)].append(partner)

for room in roomList:
    print(f'There are {len(room)} in this room.')
    print(f'They are {room}.')

print(roomList)
