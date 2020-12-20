import random


def main():
    n = int(input("Строки и столбцы \n"))

    matrix = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    print(*matrix, sep='\n')


if __name__ == '__main__':
    main()