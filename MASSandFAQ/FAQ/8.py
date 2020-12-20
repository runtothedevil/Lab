a=[1,2,3,1,2,3]
b=set()
c=[]
for i in a:
    if i not in b:
        b.add(i)
        c.append(i)
print(c)