# 集合 数据去重 数据无序 可变类型数据
# 创建集合
numSet = {10, 20, 30, 40, 50, 10, 30}
print(numSet)

stringSet = set('Orlando')
print(stringSet)

emptySet = set()
print(emptySet)
print(type(emptySet))

# 增加
# add() 增加单一数据
numSet.add(60)
print(numSet)

numSet.add(50)
print(numSet)

# update() 增加数据序列
numSet.update([70, 80, 90, 100, 20])
print(numSet)

# 删除
# remove() 删除指定数据，不存在则报错
numSet.remove(10)
print(numSet)

# discard() 删除指定数据，不存在不报错
numSet.remove(20)
print(numSet)

# pop() 随机删除某个元素
print(numSet.pop())
print(numSet)

# 查找
print(10 in numSet)
print(20 not in numSet)
