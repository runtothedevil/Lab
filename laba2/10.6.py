a=0
c=0
while a!='':
    a=input('Введите число ')
    if a=='Стоп':
        break
    else:
        a=int(a)
    c=c+a
print(c)