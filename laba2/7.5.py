import doctest

def a(x):
    b = x ** 4 + 4 ** x
    return b


x = int(input('Введите число: '))
print(doctest.testmod(a(x)))