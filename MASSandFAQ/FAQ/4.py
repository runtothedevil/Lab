def find_pairs(L,summ):
    s = set(L)
    edgeCase = summ/2
    if L.count(edgeCase) ==2:
        print (edgeCase, edgeCase)
    s.remove(edgeCase)
    for i in s:
        diff = summ-i
        if diff in s:
            print (i, diff)

L = [6,7,9,1,2,4,7,6,7,5,8]
summ = 12
find_pairs(L,summ)