import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

#Gil Ernesto Leite Guedes
#125031

#a
def minimos_quadrados(x, y):
    # Número de pontos
    N = x.size
    
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x ** 2)
    sum_y2 = np.sum(y ** 2)
    sum_xy = np.sum(x * y)

    # Coeficientes da reta
    m = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x ** 2)
    b = (sum_x2 * sum_y - sum_x * sum_xy) / (N * sum_x2 - sum_x ** 2)

    # Coeficiente de determinação
    r2 = ((N * sum_xy - sum_x * sum_y) ** 2) / ((N * sum_x2 - sum_x ** 2) * (N * sum_y2 - sum_y ** 2))

    # Incertezas
    dm = np.abs(m) * np.sqrt((1 / r2 - 1) / (N - 2))
    db = dm * np.sqrt(sum_x2 / N)

    return m, b, r2, dm, db

x = np.array([1.2, 4.2,11,20,22,37,45])#comprimento do Femur  cm
y = np.array([0.03,0.54,9.1,38,57,230,480])#Massa   Kg
m,b,r2,dm,db = minimos_quadrados(x,y)

plt.figure()
plt.plot(x, y, 'o')
plt.plot(x, x*m+b, label='Ajuste')
plt.xlabel("comprimento do Femur (cm)")
plt.ylabel("Masssa (Kg)")
plt.title('Gráfico da Massa em funçao do Comprimento do Femur')
plt.show()

#Coeficiente de determinação (r²) = 0.8151276625448709