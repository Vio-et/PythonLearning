# Python运算符 -- () 高于 ** 高于 * / // % 高于 +-
num, float1, str1 = 10, 5.6, 'Hello Orlando'
print(num)
print(float1)
print(str1)

# += 和 + 谁的优先级更高 ?
c = 10
c += 1 + 2
print(c)
# + 优先级更高
d = 10
d *= 1 + 2
print(d)

one = 1
two = 2
three = 3

print((one < two) and (three > two))
print((one >= two) or (three <= two))
print(not ((one < two) and (three > two)))

# 数字之间的and： 若有一个为0，则为0；否则返回最后一个非0数字
# 数字之间的or： 只有所有值为0，则为0；否则返回第一个非0数字
