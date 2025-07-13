import numpy as np
import matplotlib.pyplot as plt

N = 10

X = np.random.normal(4.5,0.5,size=N)
Xmedia = np.mean(X)
Xerro = np.std(X)/np.sqrt(N)

Y = np.random.normal(10,1,size=N)
Ymedia = np.mean(Y)
Yerro = np.std(Y)/np.sqrt(N)

Z = X+Y
Zmedia = np.mean(Z)

#i
sol1z = np.std(Z) / np.sqrt(N)

#ii
sol2z = np.sqrt(Xerro**2 + Yerro**2)

W = X*Y
Wmedia = np.mean(W)

#i
sol1w = np.std(W) / np.sqrt(N)

#ii
sol2w = Wmedia * np.sqrt((Xerro / Xmedia) ** 2 + (Yerro / Ymedia) ** 2) 


sol1 = (sol1z + sol1w) /2
sol2 = (sol2z + sol2w) /2
print(sol1)
print(sol2)

print((sol2/sol1)*100)
