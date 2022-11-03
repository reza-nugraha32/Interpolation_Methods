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

x_i = [x0, x1, x2, x3]
f_xi = [f_x0, f_x1, f_x2, f_x3]
m_i = np.zeros(4)

for i in range(3):
    m_i[i] = (f_xi[i+1] - f_xi[i])/(x_i[i+1] - x_i[i])

l_1 = np.arange(x0, x1, 0.01)
l_2 = np.arange(x1, x2, 0.01)
l_3 = np.arange(x2, x3, 0.01)
line_1 = f_x0 + m_i[0]*(l_1-x0)
line_2 = f_x1 + m_i[1]*(l_2-x1)
line_3 = f_x2 + m_i[2]*(l_3-x2)

if x_input < x1 :
  y = f_x0 + m_i[0]*(x_input-x0)
elif x_input < x2 :
  y = f_x1 + m_i[1]*(x_input-x1)
elif x_input < x3 :
  y = f_x2 + m_i[2]*(x_input-x2)

print("Nilai interpolasi : f("+str(x_input)+") = "+str(y))
plt.plot(x_input, y, "ro", l_1, line_1, l_2, line_2, l_3, line_3)
plt.show()