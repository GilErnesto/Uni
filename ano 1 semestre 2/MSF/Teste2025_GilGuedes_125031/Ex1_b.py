import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

#Gil Ernesto Leite Guedes
#125031

#b
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

#logaritmo da Massa
logy = np.log(y) 
m, b, r2, dm, db = minimos_quadrados(x, logy)

plt.figure()
plt.plot(x, logy, 'o')  
plt.plot(x, m * x + b, 'r-', label="Ajuste")
plt.legend()
plt.xlabel("comprimento do Femur (cm)")
plt.ylabel("Masssa (Kg)")
plt.title('Gráfico do logaritmo da Massa em funçao do Comprimento do Femur')
plt.show()

#m = 0.19329499827571386         #erro m = 0.038411731742998514        
#Coeficiente de determinação (r²) = 0.8351081253935738


#logaritmo do FEmur e MAssa
logx = np.log(x)
logy = np.log(y)
m, b, r2, dm, db = minimos_quadrados(logx, logy)

plt.figure()
plt.plot(logx, logy, 'o')  
plt.plot(logx, m * logx + b, 'r-', label="Ajuste")
plt.legend()
plt.xlabel("comprimento do Femur (cm)")
plt.ylabel("Masssa (Kg)")
plt.title('Gráfico do logaritmo da Massa em funçao do logaritmo do Comprimento do Femur')
plt.show()

#m = 2.6669805798913058         #erro m = 0.05887341253330232          
#Coeficiente de determinação (r²) = 0.9975694092514619