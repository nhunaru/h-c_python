import math
x1=float(input("nhap gtri x1:"))
y1=float(input("nhap gtri y1:"))
x2=float(input("nhap gtri x2:"))
y2=float(input("nhap gtri y2:"))
x3=float(input("nhap gtri x3:"))
y3=float(input("nhap gtri y3:"))
a=math.sqrt((x2-x1)**2+(y2-y1)**2)
b=math.sqrt((x3-x1)**2+(y3-y1)**2)
c=math.sqrt((x3-x2)**2+(y3-y2)**2)
if not (a+b>c and a+c>b and b+c>a) :
    print("3 diem da cho ko tao thanh tam giac")
else:
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"chu vi cuar tam giac la:{a+b+c:.2f}")
    print(f"dien tich tam giac la:{s:.2f}")