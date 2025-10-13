x1=int(input("Введите кооординату x1 "))
y1 = int(input("Введите координату y1"))
x2=int(input("Введите кооординату x2 "))
y2=int(input("Введите кооординату y2 "))
if (x1>0 and y1>0):
    quarter1=1
elif (x1<0 and y1>0):
    quarter1=2
elif (x1<0 and y1<0):
    quarter1=3
elif (x1>0 and y1<0):
    quarter1=4
if (x2>0 and y2>0):
    quarter2=1
elif (x2<0 and y2>0):
    quarter2 = 2
elif (x2<0 and y2<0):
    quarter2 = 3
elif (x2>0 and y2<0):
    quarter2 = 4
if quarter1 == quarter2:
    print("YES", quarter1)
else:
    print("NO")