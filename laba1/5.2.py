a=float(input('Введите первое число : '))
b=float(input('Введите второе число : '))
def two_numbers(a, b):
    if a>b:
        print('Наибольшее число = ',a)
    elif b>a :
        print('Наибольшее число = ',b)
    else:
        print('Числа равны')