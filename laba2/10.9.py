t=input("Введите текст ")
ls=[]
k=0
s=0
for i in t:
    if i in '1234567890':
        ls.append(int(i))
        k=k+1
        s=s+int(i)
print("Все сущ цифры:")
print(ls)
print("Их кол-во:")
print(k)
print("Их сумма: ")
print(s)
print("Их максимум: ")
print(max(ls))