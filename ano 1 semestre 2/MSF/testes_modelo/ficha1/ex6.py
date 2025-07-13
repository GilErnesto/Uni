import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

#array
x = np.array([1,2,3,4,5,6,7,8,9,10])                                               #tempo em minutos
y = np.array([0, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.66, 6.329]) #distancia em Km
N = len(x) #number of points

#calc
m = (N * np.sum(y*x) - np.sum(x)*np.sum(y))/(N*(np.sum(y**2)) - (np.sum(y))**2)
b = (np.sum(y**2)*np.sum(y) - np.sum(y)*np.sum(y*y))/(N * np.sum(y**2) - (np.sum(y))**2)
print(f'reta de ajuste = {m:.9f}x + {b:.9f}')
r2 = (N * np.sum(x*y) - np.sum(x)*np.sum(y))**2 / ((N*(np.sum(x**2)) - (np.sum(x))**2) * (N*(np.sum(y**2)) - (np.sum(y))**2))
print(f'r² = {r2:.9f}')
delta_m = np.abs(m) * np.sqrt(((1/r2) - 1) / (N - 2))
delta_b = delta_m * np.sqrt(np.sum(y**2)/N)
print(f'delta de m = {delta_m:.9f} --- delta de b = {delta_b:.9f}')

#plot
plt.figure()
plt.plot(x,y, 'o')
plt.show()

#c
x_medio = np.mean(x)/N #minutos
y_medio = np.mean(y)/N #km

x_medio = x_medio / 60 #horas

v_media = y_medio / x_medio #km/h
print(f'v_media = {v_media:.9f} km/h')

#d
coef = np.polyfit(x, y, 1)  #método dos mínimos quadrados para ajustar um polinômio de grau 1 (reta) aos dados fornecidos nos arrays x e y
declive = coef[0]  #declive da reta
ordenada = coef[1] #ordenada na origem da reta
print(f"Declive = {declive:.9f}")
print(f"Ordenada na origem = {ordenada:.9f}")