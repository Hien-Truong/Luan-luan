'''input: A=[a_1,a_2] và B=[b_1;b_2]
            alpha và beta
    Output: A và B có xảy ra quan hệ alpha-beta không'''
from fractions import Fraction
import numpy as np

def get_float_input(prompt):
    '''Ham de nhap gia tri so thuc tu nguoi dung, ho tro ca so nguyen va phan so'''
    while True:
        input_value = input(prompt)
        try:
            if '.' in input_value:
                return float(input_value)
            else:
                return float(Fraction(input_value))
        except ValueError:
            print("Giá trị nhập vào không hợp lệ. Vui lòng thử lại.")

def validate_alpha_beta(value):
    """Kiểm tra xem giá trị alpha và beta có nằm trong khoảng [0, 1] hay không."""
    if not (0 <= value <= 1):
        raise ValueError("Giá trị phải nằm trong khoảng [0, 1].")
# Dinh nghi ham tinh toan
def K(x, y, alpha):
    """Tính toán giá trị K dựa trên x, y và alpha."""
    return (1 - alpha) * x + alpha * y

# Nhập alpha và beta
alpha = get_float_input("Nhập giá trị alpha: ")
validate_alpha_beta(alpha)  # Kiểm tra giá trị alpha

beta = get_float_input("Nhập giá trị beta: ")
validate_alpha_beta(beta)  # Kiểm tra giá trị beta

# Nhập 2 đoạn số cần so sánh
input_strA = input("Nhập cận dưới và cận trên của đoạn A (cách nhau bởi khoảng trắng): ")
input_strB = input("Nhập cận dưới và cận trên của đoạn B (cách nhau bởi khoảng trắng): ")

# Chuyển đổi đầu vào thành float
a_1, a_2 = map(float, input_strA.split())
b_1, b_2 = map(float, input_strB.split())

# Tính K_alpha và K_beta của các đoạn A và B
K_alpha_A = K(a_1, a_2, alpha)
K_beta_A = K(a_1, a_2, beta)
K_alpha_B = K(b_1, b_2, alpha)
K_beta_B = K(b_1, b_2, beta)

# Kết quả
A = np.arange(a_1, a_2 , 0.0001, dtype=float)
B = np.arange(b_1, b_2 , 0.0001, dtype=float)
print("Tập ràng buộc các giá trị là A=",A)
print("Tập ràng buộc các giá trị là B=",B)
if (K_alpha_A < K_alpha_B) or (K_alpha_A == K_alpha_B and K_beta_A <= K_beta_B):
    print("A <= (alpha_beta) B")
else:
    print("B <= (alpha_beta) A")