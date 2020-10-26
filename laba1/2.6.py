def m(s):
    while s>3600:
        s=s-3600
    minut=s//60
    print(minut)
s=int(input('Введите секунды:'))
m(s)