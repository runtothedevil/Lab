def Arif(a, b, c):
    Sr = (a + b + c) / 3
    print('Среднее арифметическое чисел ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' =', Sr)


a, b, c = map(int, input('Введите три числа:').split())
Arif(a, b, c)
