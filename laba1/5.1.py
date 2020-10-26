m=int(input('Введите массу тела  : '))
r=int(input('Введите  рост  : '))
index= round(m/((r/100)**2))
if index<16:
    print(index,'Выраженный дефицит массы тела')
elif (index>16) and (index<18.5):
    print(index,'Недостаточная (дефицит) масса тела')
elif (index>=18.5) and (index<25):
    print(index,'Норма')
elif (index>=25) and (index<30):
    print(index,'Избыточная масса тела (предожирение)')
elif (index>=30) and (index<35):
    print( index,'Ожирение')
elif index>=35 and (index<40):
    print(index,'Ожирение резкое')
elif index>=40:
    print(index,'Очень резкое ожирение')
