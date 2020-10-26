def number(a):
    if a / 2 == 0 :
        return ("Введенное число четное")
    else:
        return ("Введенное число нечетное")
a=int(input('Введите число : '))
print(number(a))