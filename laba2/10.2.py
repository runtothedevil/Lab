L = [-8, 8, 6.0, 5, 'строка', -3.1]
S=0
for i in range(0,len(L),1):
    if type(L[i]) == int or type(L[i]) == float:
        S=S+L[i]
print(S)