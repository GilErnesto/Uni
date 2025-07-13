import numpy as np

a = np.zeros(3)    # 1D array of 3 zeros, float
b = np.zeros((3, 4))  # 2D array of shape (3, 4) of zeros, float
c = np.zeros((3, 4), dtype=int)  # 2D array of shape (3, 4) of zeros, int

d = np.ones(3)   # 1D array of 3 ones, float    

e = np.empty(3)  # 1D array of 3 uninitialized values, float

f = np.linspace(2, 10, 5)  # 1D array of 5 values from 2 to 10, float

e = np.array([10,20]) # 1D array of 2 values, int

lista = [1, 2, 3]
g = np.array(lista)  # Convert list to array, int
h = np.array(lista, dtype=float)  # Convert list to array, float

np.random.seed(0)  # Set seed for reproducibility
i = np.random.randint(10, size=6)  # 1D array of 6 random integers from 0 to 9
j = np.random.randint(10, size=(3, 4))  # 2D array of shape (3, 4) random integers from 0 to 9


k = np.sin(i)  # Apply sine function to each element of i   
l = np.cos(j)  # Apply cosine function to each element of j
m = np.exp(i)  # Apply exponential function to each element of i
n = np.sqrt(i)  # Apply square root function to each element of i
o = np.log(i)  # Apply logarithm function to each element of i
p = np.abs(i)  # Apply absolute function to each element of i
q = np.sum(i)  # Sum of all elements in i
r = np.mean(i)  # Mean of all elements in i                                  MÉDIA
s = np.std(i)  # Standard deviation of all elements in i                     DESVIO PADRÃO
t = np.var(i)  # Variance of all elements in i                               VARIÂNCIA
w = np.median(i)  # Median of all elements in i                              MEDIANA
u = np.min(i)  # Minimum value of i
v = np.max(i)  # Maximum value of i
x = np.sort(i)  # Sort i in ascending order
y = np.argsort(i)  # Indices that would sort i                              
z = np.unique(i)  # Unique elements of i
aa = np.concatenate((i, j.flatten()))  # Concatenate i and flattened j
ab = np.vstack((i, j.flatten()))  # Stack i and flattened j vertically       Empilha i e j achatado verticalmente
ac = np.hstack((i, j.flatten()))  # Stack i and flattened j horizontally     Empilha i e j achatado horizontalmente
ad = np.where(i > 5, 4, 0)  # Indices of elements in i greater than 5        

