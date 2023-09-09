# 推导式 —— list dict set
# list derivation 控制有规律的列表
numList = []
i = 0
while i < 10:
    numList.append(i)
    i += 1

print(numList)

numList.clear()

for num in range(0, 10):
    numList.append(num)

print(numList)

numList.clear()

numList = [i for i in range(10)]
print(numList)

numList.clear()

numList = [i for i in range(0, 10, 2)]
print(numList)

numList.clear()

for i in range(10):
    if i % 2 == 0:
        numList.append(i)

print(numList)

numList.clear()

numList = [i for i in range(10) if i % 2 == 0]
print(numList)

locList = []

for i in range(1, 3):
    for j in range(3):
        locList.append((i, j))

print(locList)

locList.clear()

locList = [(i, j) for i in range(1, 3) for j in range(3)]
print(locList)

# dict derivation 快速合并字典 和 提取数据
squareDict = {i: i ** 2 for i in range(1, 5)}
print(squareDict)

cubeDict = {i: i ** 3 for i in range(5, 10)}
print(cubeDict)

nameList = ['Orlando', 'Arthur', 'Sasuke']
partnerList = ['Violet', 'Rebeca', 'Sakura']

# 两列表合并，长度取小的列表
mergeDict = {nameList[i]: partnerList[i] for i in range(len(nameList))}
print(mergeDict)

biggerDict = {key: value for key, value in squareDict.items() if value > 5}
print(biggerDict)

# set derivation
numSet = {i ** 2 for i in numList}
print(numSet)
