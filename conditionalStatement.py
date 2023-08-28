import random

# if statement
"""
if 条件：
    条件成立时执行的代码
    ......
"""
if True:
    print('Get in if statement')

# input输入的数据类型是str，不能和18作判断
age = int(input('Please enter your age.\n'))
if age >= 18:
    print(f'Your age is {age}, you are an adult!')
else:
    print(f'Your age is {age}, you are a teenager')


# if...else... statement
"""
if 条件：
    条件成立时执行的代码
    ......
else ：
    条件不成立时执行的代码
    ......
"""

# 多重判断
"""
if 条件1：
    条件1成立时执行的代码
    ......
elif 条件2：
    条件2成立时执行的代码
    ......
......
else:
    以上条件都不成立时执行的代码
"""
ageInt = int(input('Please input your age\n'))
if age < 18:
    print(f'Your age is {age}, it is illegal')
elif age > 60:
    print(f'Your age is {age}, it is illegal')
else:
    print(f'Your age is {age}, it is legal')

# age >= 18 and age <= 20 可以写为 18 <= age <= 20

# if 嵌套
money = int(input('Please enter your poket money.\n'))
emptySit = 0
if money >= 2:
    print(f'Your poket money is {money}, you can get in bus.')
    if emptySit > 0:
        print(f'There are {emptySit} empty sit, you can sit down')
    else:
        print(f'There are no empty sit, you must stand for a while')
else:
    print('You have no money, you can\'t get in the bus.')

gesturePlayer = int(input('Please enter your gesture in mora: 0--rock 1--scissor 2--paper\n'))
gestureMachine = random.randint(0, 2)
print(f'Machine\'s gesture is {gestureMachine}')
if gesturePlayer == gestureMachine:
    print(f'It\'s a draw.')
elif ((gesturePlayer == 0) and (gestureMachine == 1)) or ((gesturePlayer == 1) and (gestureMachine == 2)) or ((gesturePlayer == 2) and (gestureMachine == 0)):
    print('You win!')
else:
    print('You fail.')
# 随机数：导入随机模块 使用random.randint(start,end)


# 三目运算符 条件成立表达式 if 条件 else 条件不成立表达式
a = 3
b = 4
c = a - b if a > b else b - a
print(c)
