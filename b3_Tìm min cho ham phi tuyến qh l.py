'''K = { A= [ min{f_1, f_2 }] } tìm min  theo quan hệ l'''
from scipy.optimize import minimize_scalar
import numpy as np
import math
import sympy as sp
#Định nghĩa pi
p=math.pi 
def parse_function(func_str):
    """Chuyển đổi chuỗi hàm thành hàm có thể tính toán."""
    x = sp.Symbol('x')
    return sp.lambdify(x, sp.sympify(func_str), 'numpy')

# Nhập hàm F(x)=[f_1(x),f_2(x)] với các hàm f_1 và f_2 được định nghĩa sau đây:
f_1_str = input("Nhập hàm f_1 theo biến x: ")
f_2_str = input("Nhập hàm f_2 theo biến x: ")
f_1 = parse_function(f_1_str)
f_2 = parse_function(f_2_str)

#Xác định tập ràng buộc
input_str = input("Nhập cận trên và cận dưới của tập rằng buộc a, b: ")
array_float = [float(x) for x in input_str.split()]
[a,b]= array_float
D = np.arange(a, b , 0.0001, dtype=float)
print("Tập ràng buộc các giá trị là D =",D)
# Tìm giá trị nhỏ nhất của hàm f_1 trong khoảng [a, b]
result_min1 = minimize_scalar(f_1, bounds=(a, b))
result_min2 = minimize_scalar(f_2, bounds=(a, b))
result_min=min(result_min1.fun,result_min2.fun)
if result_min == result_min1.fun:
    x_min = result_min1.x
else:
    x_min = result_min2.x
# Nghiệm theo quan hệ l
A_1 = min (f_1(x_min), f_2(x_min)) 
A_2 = max (f_1(x_min), f_2(x_min)) 
print("Giá trị nhỏ nhất trong hai hàm số f_1 và f_2: ", result_min)
print("Nghiệm theo quan hệ l, x=:", x_min)
print('phần tử bé nhất là A_min = ',[A_1, A_2] )
