game=int(input("Введите количество игр \n"))
for i in range(game):
    N,K=map(int,input("Количество секторов и номер черной мишени \n").split())
    max=-100
    q=0
    a = list(map(int, input("Введите баллы за сектор \n").split()))
    if len(a)!=N:
        print('Введеено неверное количество секторов ')
        break
    else:
            a[K] = min(a)
            if a[K] > 0:
                a[K] = 0
            for i in range(N):
                sum = 0
                for j in range(N):
                    d = i + j
                    if d > N - 1:
                        d = d - N
                    sum = sum + a[d]
                    if sum > max:
                        max = sum
            print(max)
else:
            if (K == -1):
                for i in range(N):
                    sum = 0
                    for j in range(N):
                        d = i + j
                        if d > N - 1:
                            d = d - N
                        sum = sum + a[d]
                        if sum > max:
                            max = sum
                print(max)