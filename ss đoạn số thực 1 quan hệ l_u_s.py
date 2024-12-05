import numpy as np
# Tạo dữ liệu đầu vào
input_str = input("Nhập c, d, e, f: ")
array_float = [float(x) for x in input_str.split()]
[c,d,e,f]= array_float
#So sánh 2 khoảng giá trị theo các quan hệ
A = np.array([c,d])
B = np.array([e,f])
if d <= c or f <= e:
    print("Dữ liệu đầu vào sai")
else:
    print("A=",A)
    print("B=",B)
if A[0] <= B[0]  :
    print('A<= B theo quan hệ l')
    l = 1
else:
    l= 0 #không xả ra qh l giữ A và B
if A[1]<= B[1]:
    print("A <= B theo quan hệ u")
    u= 1
else:
    u= 0 #không xả ra qh u giữ A và B
if l== 1 and u==1:
    print('A <= B theo quan hệ s')
    #so sánh theo chiều ngược lại
if B[0] <= A[0]  :
    print('B <= A theo quan hệ l')
    l = 2
else:
    l= 3 #không xả ra qh l giữ B và A
if B[1]<= A[1]:
    print("B <= A theo quan hệ u")
    u= 2
else:
    u=3 #không xả ra qh u giữ B và A
if l== 2 and u==2:
    print('B <= A theo quan hệ s')