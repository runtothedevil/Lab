def F(x):
    if (x<=5.7) and (x>=-2.4):
        F=x**2
    else:
        F=4
    print('значение функции = ',F)
x=float(input('Введите число : '))
F(x)