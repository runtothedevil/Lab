import random

x = random.randint(1, 6)
y = random.randint(1, 6)
print('У первого игрока', x)
print('У второго игрока', y)
if x > y:
    print('У первого игрока больше')
else:
    print('У второго игрока больше')