colors=["red","blue","yellow"]
print(colors)
student=["an","binh","nga","phuong","thiên","thành"]
print(student[0])
print(student[2])
print(student[:])
print(student[1:2])
#chèn vào cuối chuỗi
student.append("ngọc")
#chèn vào vị trí chỉ định
student.insert(2,"nghĩa")
print(student)
print(len(student))
#đếm phần tử tỏng chuỗi
print(student.count("nghĩa"))
#xóa phần tử
if "ngọc" in student :
    student.remove("ngọc")
print(student)
student.pop(2)
print(student)