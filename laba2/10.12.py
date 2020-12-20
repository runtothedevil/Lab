from random import randint
N = int(input("Количество столбцов \n"))
M = int(input("Количество строк \n"))
lst=[[randint(1, 9) for i in range(N)] for i in range(M)]
print(lst)
for i in lst:
    print()
    for j in i:
        print (j, end=" ")
kol=0
num_str=0
for i in range(M):
    for j in range(N):
        kol_new=lst[i].count(lst[i][j])
        if kol_new>kol:
            kol=kol_new
            num_str=i
print()
print(num_str)