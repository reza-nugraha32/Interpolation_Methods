import numpy as np
import matplotlib.pyplot as plt

x0 = float(input("Masukkan titik ke-0 x0: "))
x1 = float(input("Masukkan titik ke-1 x1: "))
x2 = float(input("Masukkan titik ke-2 x2: "))
f_x0 = float(input("Masukkan nilai f(x0): "))
f_x1 = float(input("Masukkan nilai f(x1): "))
f_x2 = float(input("Masukkan nilai f(x2): "))
x_input = float(input("Masukkan titik yang ingin diinterpolasi: "))

def lagrange_orde2(x):
    f_x = (((x-x1)/(x0-x1))*((x-x2)/(x0-x2))*f_x0)+(((x-x0)/(x1-x0))*((x-x2)/(x1-x2))*f_x1)+(((x-x0)/(x2-x0))*((x-x1)/(x2-x1))*f_x2)
    return f_x

x = np.arange(x0, x2, 0.05)
y = lagrange_orde2(x_input)

line = lagrange_orde2(x)

print("Nilai interpolasi : f("+str(x_input)+") = "+str(y))
plt.plot(x_input, y, "bo", x0, f_x0, "ro", x1, f_x1, "ro", x2, f_x2, "ro")
plt.plot(x, line, "b--")
plt.show()