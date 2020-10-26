import random
a = random.randint(1,5)
b = int(input('Отгадайте число от 1 до 5: '))
if b == a:
    print ('Вы угадали! ')
else:
    print ('В следующий раз повезет! ')