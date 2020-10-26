def U(a1,b1,c1,a2,b2,c2):
    d=a1*b2-a2*b1
    x=(c1*b2-c2*b1)/d
    y=(a1*c2-a2*c1)/d
    print('x= '+str(x)+' y= ',y)
a1,a2,b1,b2,c1,c2=map(int,input('Введите коэфиценты:').split())
U(a1,b1,c1,a2,b2,c2)