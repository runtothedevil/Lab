import random
lists = ['самовар', 'весна', 'лето']
a=random.choice(lists)
b=random.choice(a)
print(a[:a.index(b)]+'?'+a[a.index(b)+1:])

c=str(input('Попытайтесь угадать букву '))
if c==b:
    print('Вы угадали')
else:
    print('Вы не угадали')