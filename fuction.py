# function 函数
"""
def functionName(parameter1, ...):
    code
    ......
"""


def select():
    print("Show your money.")
    print('Save money.')
    print('Get money')


print('Sign in successfully.')
select()

print('Your money is 10000.')
select()

print('You get 100 yuan.')
select()

# 调用函数的时候解释器会回到定义函数的位置，执行结束后回到调用函数的位置


def info():
    print('Hello world.')


info()


def addTwoNumbers(num1, num2):
    """
    Add two numbers and return their sum.
    :param num1: add number A
    :param num2: add number B
    :return: the  sum of num1 and num2
    """
    return num1 + num2


print(addTwoNumbers(20, 40))

# help(len)  help(): 查看函数的说明文档
help(addTwoNumbers)


def addThreeNumbers(num1, num2, num3):
    temp = addTwoNumbers(num1, num2)
    return addTwoNumbers(temp, num3)


print(addThreeNumbers(1, 2, 3))


def outputLine():
    print('-' * 20)


outputLine()


def outputLines(lineNum):
    i = 0
    while i < lineNum:
        outputLine()
        i += 1


outputLines(10)


def average(num1, num2, num3):
    return addThreeNumbers(num1, num2, num3) / 3


print(average(2, 4, 6))
