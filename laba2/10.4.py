from random import *

N = randint(1, 10)
K = int(input("Напишите число от 1 до 10: "))
while K != N:
    K = int(input("Попробуй снова: "))
    if K < N:
        print("Загаданное число больше.")
    elif K > N:
        print("Загаданное число меньше.")
    else:
        print("Угадал!")
        print(K)
        print(N)