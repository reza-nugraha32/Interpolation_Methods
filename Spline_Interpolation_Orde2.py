import numpy as np
import matplotlib.pyplot as plt

x0 = float(input("Masukkan titik ke-0 x0: "))
x1 = float(input("Masukkan titik ke-1 x1: "))
x2 = float(input("Masukkan titik ke-2 x2: "))
x3 = float(input("Masukkan titik ke-3 x3: "))
f_x0 = float(input("Masukkan nilai f(x0): "))
f_x1 = float(input("Masukkan nilai f(x1): "))
f_x2 = float(input("Masukkan nilai f(x2): "))
f_x3 = float(input("Masukkan nilai f(x3): "))
x_input = float(input("Masukkan titik yang ingin diinterpolasi: "))

matrix_A = np.array([[x1, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, x1**2, x1, 1, 0, 0, 0],
                     [0, 0, x2**2, x2, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, x2**2, x2, 1],
                     [x0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, x3**2, x3, 1],
                     [1, 0, -2*x1, -1, 0, 0, 0, 0],
                     [0, 0, 2*x2, 1, 0, -2*x2, -1, 0]])

matrix_B = [f_x1, f_x1, f_x2, f_x2, f_x2, f_x3, 0, 0]

solution = np.dot(np.linalg.inv(matrix_A), matrix_B)

a1 = 0
b1 = solution[0]
c1 = solution[1]
a2 = solution[2]
b2 = solution[3]
c2 = solution[4]
a3 = solution[5]
b3 = solution[6]
c3 = solution[7]

l_1 = np.arange(x0, x1, 0.01)
l_2 = np.arange(x1, x2, 0.01)
l_3 = np.arange(x2, x3, 0.01)
line_1 = (l_1**2)*a1 + l_1*b1 + c1
line_2 = (l_2**2)*a2 + l_2*b2 + c2
line_3 = (l_3**2)*a3 + l_3*b3 + c3

if x_input < x1 :
  y = (x_input**2)*a1 + x_input*b1 + c1
elif x_input < x2 :
  y = (x_input**2)*a2 + x_input*b2 + c2
elif x_input < x3 :
  y = (x_input**2)*a3 + x_input*b3 + c3

print("Nilai interpolasi : f("+str(x_input)+") = "+str(y))
plt.plot(x_input, y, "ro", l_1, line_1, l_2, line_2, l_3, line_3)
plt.show()