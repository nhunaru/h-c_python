x=int(input("nhap so nguyen x bat ki:"))
kq="so chan" if x%2==0 else "so le"
print("x la ",kq)
if x>=9:
    print("hsg")
elif x>=7:
    print("hsk")
elif x>5:
    print ("hstb")
else:
    print("hoc sinh yeu")
print ("ket thuc chuong trinh dai truyen hinh den đây là kết thúc")