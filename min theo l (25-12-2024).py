from scipy.optimize import minimize_scalar
import sympy as sp
from fractions import Fraction
import numpy as np
#Hàm kiểm tra
def get_float_input(prompt):
    """Hàm để nhập giá trị số thực từ người dùng, hỗ trợ cả số nguyên và phân số."""
    while True:
        input_value = input(prompt)
        try:
            if '.' in input_value:
                return float(input_value)
            else:
                return float(Fraction(input_value))
        except ValueError:
            print("Giá trị nhập vào không hợp lệ. Vui lòng thử lại.")
# định nghĩa hàm cho cận trên cận dưới của tập A
def parse_function(func_str):
    x = sp.Symbol('x')
    return sp.lambdify(x, sp.sympify(func_str), 'numpy')
f_1_str = input("Enter function f_1 in terms of x: ")
f_2_str = input("Enter function f_2 in terms of x: ")
f_1 = parse_function(f_1_str)
f_2 = parse_function(f_2_str)
#nhập tập ràng buộc D
a = get_float_input("nhập cận dưới của D: ")
b =  get_float_input("Nhập cận trên của D: ")
if a >= b:
    raise ValueError("Cận dưới phải bé hơn cận trên. Vui lòng thử lại!")
print(f"tập ràng buộc D: , [{a:.2f},{b:.2f}]")
D = np.arange(a, b, 0.01, dtype=float)
# Thuật toán
c = minimize_scalar(f_1, bounds=(a, b),method='bounded')
d = minimize_scalar(f_2, bounds=(a, b),method='bounded')
print('c.fun va d.fun: ', c.fun,' ', d.fun)
print('c.x va d.x: ',c.x,' ', d.x)
if c.fun <= d.fun:
    c_min = c.fun
    x_min = c.x
    d_min = f_2(x_min)
    print(f"Phần tử tối thiểu theo quan hệ l là [{c_min:.2f}, {d_min:.2f}]")
if c.fun > d.fun:
    c_min = d.fun
    x_min = d.x
    d_min = f_1(x_min)
    print(f"Phần tử tối thiểu theo quan hệ l là [{c_min:.2f}, {d_min:.2f}]")
if c.fun == d.fun:
    c_min = d_min = c.fun
    x_min = c.x
    print(f"Phần tử tối thiểu theo quan hệ l là số thực {c_min:.2f}")
print(f"Nghiệm cần tìm là {x_min:.2f}")