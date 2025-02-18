import math  
def gaipt(a,b,c):
    if a==0:
        if b==0:
            #ham bac nhat
            return "pt vo nghieem" if c!=0 else "pt co vo so nghiem"
        return f"pt co 1 nghem : x={-c/b:.2f}"
    delta=b*b-4*a*c
    if delta>0:
        x1=(-b+math.sqrt(delta))/2*a
        x2=(-b-math.sqrt(delta))/2*a
        return f"pt co 2 nghiem: x1={x1:.2f},x2={x2:.2f}"
    #:.2f dùng để cho ra kết quả với 2 số thập phân
    elif delta==0:
        x=-b/2*a
        return f"phuong trinh co 1 n0*:x={x:.2f}"
    else:
        return "pt vo nghiem"
a=float(input())
b=float(input())
c=float(input())
print(gaipt(a,b,c))
print("mai khong xong thi chet voi tao ")
print("tao đã sửa rồi nè")
