'''input: A=[min{f_1(x), f_2(x)},   max {f_1, f_2}], alpha_beta
Output: phần tử nhỏ nhất và x-argmin(A) quan hệ alpha_beta'''
'''Cac dữ liệu thử nghiệm
VD 1:
        Input: 
            alpha= 0.2, beta=0.3,f_1= x+1,  f_2 = x+2, D = [-1, 1]
        Output: [0, 1]
VD 2: 
        Input: 
            alpha= 0.2, beta=0.3,f_1= (x**2-1)**2 + 1,  f_2 = (x**2-1)**2 + 2, D = [-2, 2]
        Output: [1, 2]
VD 3:
        Input: 
            alpha= 0.2, beta=0.3,f_1= -x**2 - 1,  f_2 = x**2 - 2*x, D = [-2, 2]
        Output: [-2, -1]
    '''
from scipy.optimize import minimize_scalar
import sympy as sp
from fractions import Fraction
import numpy as np

def get_float_input(prompt):
    '''Hàm để nhập giá trị số thực từ người dùng, hỗ trợ cả số nguyên và phân số.'''
    while True:
        input_value = input(prompt)
        try:
            return float(Fraction(input_value)) if '/' in input_value else float(input_value)
        except ValueError:
            print("Giá trị nhập vào không hợp lệ. Vui lòng thử lại.")

def validate_alpha_beta(value):
    """Kiểm tra xem giá trị alpha và beta có nằm trong khoảng [0, 1] hay không."""
    if not (0 <= value <= 1):
        raise ValueError("Giá trị phải nằm trong khoảng [0, 1].")

def K(x, y, alpha):
    """Tính giá trị K_alpha."""
    return (1 - alpha) * x + alpha * y

def parse_function(func_str):
    """Chuyển đổi chuỗi hàm thành hàm có thể tính toán."""
    x = sp.Symbol('x')
    return sp.lambdify(x, sp.sympify(func_str), 'numpy')

def main():
    # Nhập hàm f_1 và f_2
    f_1_str = input("Nhập hàm f_1 theo biến x: ")
    f_2_str = input("Nhập hàm f_2 theo biến x: ")
    f_1 = parse_function(f_1_str)
    f_2 = parse_function(f_2_str)

    # Nhập giá trị alpha và beta
    alpha = get_float_input("Nhập giá trị alpha (0 <= alpha <= 1): ")
    validate_alpha_beta(alpha)
    beta = get_float_input("Nhập giá trị beta (0 <= beta <= 1): ")
    validate_alpha_beta(beta)

    # Nhập cận dưới và cận trên của D
    a = get_float_input("Nhập cận dưới của D: ")
    b = get_float_input("Nhập cận trên của D: ")
    if a >= b:
        raise ValueError("Cận dưới phải bé hơn cận trên. Vui lòng thử lại!")

    print(f"Tập ràng buộc D: [{a:.2f}, {b:.2f}]")

    # Tìm giá trị nhỏ nhất của K_alpha
    result_min = minimize_scalar(lambda x: K(f_1(x), f_2(x), alpha), bounds=(a, b), method='bounded')
    print("Giá trị nhỏ nhất K_alpha: ", round(result_min.fun, 6))
    x_0 = result_min.x

    # Tìm tất cả các x để K_alpha đạt giá trị nhỏ nhất
    x = sp.Symbol('x')
    eq = K(f_1(x), f_2(x), alpha) - K(f_1(x_0), f_2(x_0), alpha)
    solutions = sp.solve(eq, x)

    # Lọc bỏ các nghiệm trùng lặp
    rounded_solutions = sorted(set(round(sol.evalf(), 4) for sol in solutions))
    print("Danh sách giá trị của argmin K_alpha:", rounded_solutions)
    print("Số phần tử của argmin: ", len(rounded_solutions))

    # Tạo mảng các giá trị K_beta tương ứng với các x tìm được
    M = np.array([K(f_1(sol), f_2(sol), beta) for sol in rounded_solutions])
    print("Các K_beta tương ứng với argmin K_alpha là tập M:", M)

    # Tìm phần tử nhỏ nhất của M
    min_M = min(M)
    print("Phần tử nhỏ nhất của M: ", min_M)

    # Trả về giá trị x_min là giá trị để K_beta nhỏ nhất
    index_of_min = np.argmin(M)  # Sử dụng np.argmin để tìm chỉ số
    x_min = rounded_solutions[index_of_min]
    print("Giá trị x tương ứng x_min= ", x_min)

    # Xuất ra đoạn số thực nhỏ nhất A = [f_1(x_min), f_2(x_min)]
    A = [f_1(x_min),f_2(x_min)]
    print("Đoạn số thực nhỏ nhất theo quan hệ alpha_beta là A = ", A)

if __name__ == "__main__":
    main()