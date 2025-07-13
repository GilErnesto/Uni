import numpy as np
import matplotlib.pyplot as plt

def interpolation(x, m, b):
    return m*x+b
    
#dados de entrada
x = [2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0]                 #l
y = [222.0, 207.5, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0]  #x
N = len(x)
x = np.array(x)
y = np.array(y)

#somas
sum_x = np.sum(x).astype(float)
sum_y = np.sum(y).astype(float)
sum_x2 = np.sum(x**2).astype(float)
sum_y2 = np.sum(y**2).astype(float)
sum_xy = np.sum(x*y).astype(float)

#dados que se quer
m = ((N*sum_xy - sum_x*sum_y)/(N*sum_x2 - sum_x**2))
b = ((sum_y*sum_x2 - sum_x*sum_xy)/(N*sum_x2 - sum_x**2))
r2 = (((N*sum_xy - sum_x*sum_y)**2)/((N*sum_x2 - sum_x**2)*(N*sum_y2 - sum_y**2)))
delta_m = (abs(m)*np.sqrt((1-r2)/(N-2)))
delta_b = (delta_m*(np.sqrt(sum_x2/N)))

#print
print(f"m = {m:.3f} +- {delta_m:.3f}")
print(f"b = {b:.3f} +- {delta_b:.3f}")
print(f"r2 = {r2:.3f}")

#plot
plt.plot(x, y, marker='o', linestyle='-')
plt.plot(x, m*x+b, color='r', linestyle='-')
plt.show()
print(interpolation(165, m, b))
