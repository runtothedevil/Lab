def text(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s


s = str(input('Введите строку: '))
n = int(input('Введите значение: '))
print(text(s, n))