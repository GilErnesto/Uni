import numpy as np
import matplotlib.pyplot as plt

#dados de entrada
x = np.array(list(map(float, input("x: ").split())))
y = np.array(list(map(float, input("y: ").split())))
N = len(x)

#somas
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x**2)
sum_y2 = np.sum(y**2)
sum_xy = np.sum(x*y)

#dados que se quer
m = (N*sum_xy - sum_x*sum_y)/(N*sum_x2 - sum_x**2)
b = (sum_y*sum_x2 - sum_x*sum_xy)/(N*sum_x2 - sum_x**2)
r2 = ((N*sum_xy - sum_x*sum_y)**2)/((N*sum_x2 - sum_x**2)*(N*sum_y2 - sum_y**2))
delta_m = abs(m)*np.sqrt((1-r2)/(N-2))
delta_b = delta_m*(np.sqrt(sum_x2/N))

#print
print(f"m = {m:.3f} +- {delta_m:.3f}")
print(f"b = {b:.3f} +- {delta_b:.3f}")
print(f"r2 = {r2:.3f}")
