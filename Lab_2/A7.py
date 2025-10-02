x1=int(input("Введите координату x1 : "))
y1=int(input("Введите координату y1 : "))
x2=int(input("Введите координату x2 : "))
y2=int(input("Введите координату y2 : "))
color1=(x1 + y1) % 2
color2=(x2 + y2) % 2
if color1 == color2:
    print("YES")
    print("White" if color1 == 0 else "Black")
else:
    print("NO")