# 循环： 使得代码更高效的重复执行
# while 循环
"""
while condition:
    条件成立重复执行的代码
    ......
"""
times = 5
while times > 0:
    print(f'It\'s the {times} circle.')
    times -= 1
print('Done!')
# python 没有 i++ and i--

result = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print(f'The value of 1 plus 2 plus 3 ... to 100 is {result}.')

# break 终止整个循环 continue 跳过单次循环
# break
j = 1
while j <= 5:
    if j <= 3:
        print(f'Eating {j} apples.')
    else:
        print('Full.')
        break
    j += 1

# continue 会跳过本次循环之后的代码， 注意循环变量是否被跳过
k = 0
while k < 5:
    k += 1
    if k == 3:
        print(f'It\'s {k} apples. It hava a bug.')
        continue
    print(f'Eating {k} apples.')

# while 循环嵌套
"""
while condition:
    条件成立重复执行的代码
    ......
    while condition:
        条件成立重复执行的代码
        ......
    ......
"""
days = 0
while days < 3:
    print(f'It\'s {days + 1} day')
    i = 0
    while i < 3:
        print('Let\'s go to park together.')
        i += 1
    print('Wash feet.')
    days += 1

# 打印5*5矩阵的星星
i = 0
while i < 5:
    j = 0
    while j < 5:
        print('*', end='')
        j += 1
    print()
    i += 1

# 打印三角形的星星
i = 0
while i < 5:
    j = 0
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1

# 打印九九乘法表
item = 1
while item <= 9:
    var = 1
    while var <= item:
        print(f'{var} * {item} = {var * item}', end='\t')
        var += 1
    print()
    item += 1

# for 循环
"""
for 临时变量 in 序列:
    重复执行的代码
    ......
"""
name = 'Orlanvdo'
for i in name:
    if i == 'v':
        continue
    print(i)

# 循环 与 else 配合使用, else 下方正常结束{条件不成立、continue}之后要执行的代码，非正常结束{break}时不执行
# while ... else ...
"""
while condition:
    条件成立时重复执行的代码
    ......
else:
    循环正常结束时执行的代码
    ......
"""
times = 0
while times < 5:
    if times == 2:
        print('Not satisfied.')
        times += 1
        continue
    print(f'Let\'s go to park {times + 1} times.')
    times += 1
else:
    print('Happy ending.')

# for ... else ...
"""
for 临时变量 in 序列：
    重复执行的代码
    ......
else:
    循环正常结束时执行的代码
    ......
"""
name = 'Orlanvdo'
for i in name:
    if i == 'v':
        continue
    print(i)
else:
    print('Normal ending')

