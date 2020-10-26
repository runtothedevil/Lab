import math

def p(x):
    q = math.sqrt (1 - math.sin(x))
    return q

x = float(int(input('Введите значение х ')))
print ('Ответ ', p(x))