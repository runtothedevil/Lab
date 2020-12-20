a = int(input('Введите число '))
d = a
f = 0
c = 0
k = d % 10
if d % 10 % 2 == 1:
    f = f + k ** 2
while a != 0:
    a = a // 10
    c = c + 1
for i in range(c - 1):
    d = d // 10
    b = d % 10
    if b % 2 == 1:
        f = f + b ** 2
print(f)
