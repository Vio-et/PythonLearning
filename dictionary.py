# 字典 dictionary 可变数据类型
# key-value 键值对 用逗号隔开
userDictionary = {'name': 'Orlando', 'age': 20, 'gender': 'boy'}
print(userDictionary)
print(type(userDictionary))

emptyDictionary = {}
emptyDictionary1 = dict()
print(type(emptyDictionary))
print(type(emptyDictionary1))

# 添加
userDictionary['Partner'] = 'Violet'
print(userDictionary)

userDictionary['Partner'] = 'Sakura'
print(userDictionary)

# 删除
# del() / del
# del(userDictionary)
del userDictionary['age']
print(userDictionary)

# clear() 清空
# userDictionary.clear()
print(userDictionary)

# 修改
userDictionary['Partner'] = 'Violet'
print(userDictionary)

# 查找
# key值 查找
print(userDictionary['name'])

# get(key, default return)
partner = userDictionary.get('Partners', 'There is no this key.')
print(partner)

# keys() 得到所有的 键
print(userDictionary.keys())

# values() 得到所有的 值 返回一个list，list中为所有的 值
print(userDictionary.values())

# items() 得到所有的键值对 返回一个list，list中为所有的 键值对（元组格式）
print(userDictionary.items())

# 循环遍历
# 遍历 keys
for key in userDictionary.keys():
    print(key)

# 遍历 values
for value in userDictionary.values():
    print(value)

# 遍历 key-value
for item in userDictionary.items():
    print(item)

# 拆分 将items()的元组，元组的两个数据分别赋值给两个循环变量
for key, value in userDictionary.items():
    print(f'{key} = {value}')
