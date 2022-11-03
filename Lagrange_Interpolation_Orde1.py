import numpy as np
import matplotlib.pyplot as plt

x0 = float(input("Masukkan titik ke-0 x0: "))
x1 = float(input("Masukkan titik ke-1 x1: "))
f_x0 = float(input("Masukkan nilai f(x0): "))
f_x1 = float(input("Masukkan nilai f(x1): "))
x_input = float(input("Masukkan titik yang ingin diinterpolasi: "))

def lagrange_orde1(x):
    f_x = (((x-x1)/(x0-x1))*f_x0)+(((x-x0)/(x1-x0))*f_x1)
    return f_x

x = np.arange(x0, x1, 0.01)
y = lagrange_orde1(x_input)

line = lagrange_orde1(x)

print("Nilai interpolasi : f("+str(x_input)+") = "+str(y))
plt.plot(x_input, y, "bo", x0, f_x0, "ro", x1, f_x1, "ro")
plt.plot(x, line, "b--")
plt.legend(str(y))
plt.show()