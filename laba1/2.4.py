def S(a,b,c):
    Sr=(a+b+c)/3
    print('Сред. арифметическое = ',Sr)

print('Введите 3 числа')
a,b,c=map(int,input().split())
S(a,b,c)