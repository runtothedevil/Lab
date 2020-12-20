k=input("Введите текст: ")
d=k.split()
maxx=""
for i in range(len(d)):
    q=len(d[i])
    if q>len(maxx):
        maxx=d[i]
print(maxx)