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

b0 = f_x0
b1 = (f_x1-f_x0)/(x1-x0)
b2 = (((f_x2-f_x1)/(x2-x1))-b1)/(x2-x0)
f_x3_x2 = (f_x3-f_x2)/(x3-x2)
f_x2_x1 = (f_x2-f_x1)/(x2-x1)
b3 = (((f_x3_x2-f_x2_x1)/(x3-x1))-b2)/(x3-x0)

def newton_orde3(x):
    f_x = b0 + b1*(x-x0) + b2*(x-x0)*(x-x1) + b3*(x-x0)*(x-x1)*(x-x2)
    return f_x

x = np.arange(x0, x3, 0.01)
y = newton_orde3(x_input)

line = newton_orde3(x)

print("Nilai interpolasi : f("+str(x_input)+") = "+str(y))
plt.plot(x_input, y, "bo", x0, f_x0, "ro", x1, f_x1, "ro")
plt.plot(x, line, "b--")
plt.show()