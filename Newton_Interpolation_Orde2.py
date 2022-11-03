import numpy as np
import matplotlib.pyplot as plt

x0 = float(input("Masukkan titik ke-0 x0: "))
x1 = float(input("Masukkan titik ke-1 x1: "))
x2 = float(input("Masukkan titik ke-2 x2: "))
f_x0 = float(input("Masukkan nilai f(x0): "))
f_x1 = float(input("Masukkan nilai f(x1): "))
f_x2 = float(input("Masukkan nilai f(x2): "))
x_input = float(input("Masukkan titik yang ingin diinterpolasi: "))

b0 = f_x0
b1 = (f_x1-f_x0)/(x1-x0)
b2 = (((f_x2-f_x1)/(x2-x1))-b1)/(x2-x0)

def newton_orde2(x):
    f_x = b0 + b1*(x-x0) + b2*(x-x0)*(x-x1)
    return f_x

x = np.arange(x0, x2, 0.01)
y = newton_orde2(x_input)

line = newton_orde2(x)

print("Nilai interpolasi : f("+str(x_input)+") = "+str(y))
plt.plot(x_input, y, "bo", x0, f_x0, "ro", x1, f_x1, "ro")
plt.plot(x, line, "b--")
plt.show()