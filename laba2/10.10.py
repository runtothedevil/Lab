import random


def main():
    n = int(input("Количество строк \n"))
    m = int(input("Количество столбцов \n"))

    matrix = [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]
    print(*matrix, sep='\n')


if __name__ == '__main__':
    main()