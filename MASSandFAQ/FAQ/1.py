mass = [i for i in range(1, 101)]
del mass[21]
for k in range(len(mass)):
    a = 5050 - sum(mass)
print(a)