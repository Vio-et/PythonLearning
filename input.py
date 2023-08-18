# input函数把所有输入的数据都当作字符串处理
price = input("Please enter the price.\n")
print(f'The price is {price}')
print(type(price))

# 数据类型转换
priceInt = int(price)
print(type(priceInt))
# float change
num = 1
str1 = '10'

print(type(float(num)))
print(type(float(str1)))
print(type(str(num)))

list1 = [10, 20, 30]
print(type(tuple(list1)))

tuple1 = (100, 200, 300)
print(type(list(tuple1)))

str2 = '1'
str3 = '1.1'
str4 = '(1, 2, 3)'
str5 = '[10, 11, 12]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
