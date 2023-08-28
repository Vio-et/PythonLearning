# Python运算符
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
