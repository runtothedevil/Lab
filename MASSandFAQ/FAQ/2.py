mas=[1,2,3,4,5,6,7,8,9,10]
mas.append(1)

mas.sort()
for i in range(len(mas)-1):
    if mas[i]==mas[i+1]:
        print(mas[i])