import numpy as np
import matplotlib.pyplot as plt


 
N_values = range(10, 10001, 10)

medias = []
incertezas = []

for N in N_values:
    X = np.random.normal(4.5,0.5,size=N)
    Xmedia = np.mean(X)
    Xerro = np.std(X)/np.sqrt(N)
    medias.append(Xmedia)
    incertezas.append(Xerro)



plt.plot(N_values, medias)
plt.show()

