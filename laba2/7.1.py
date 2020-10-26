import math
def formula(p):
    p = (a + b + c) / 2
    s = float(math.sqrt(p * (p - a) * (p - b) * (p - c)))
    return s

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))
p = (a + b + c) / 2
print('Площадь треугольника равна: ', round(formula(p), 2))