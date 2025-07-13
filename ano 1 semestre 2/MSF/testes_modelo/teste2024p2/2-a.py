import numpy as np
import matplotlib.pyplot as plt


m = 0.5 #Kg
k = 2   #J/m^4

#Fx = -4 * k * x**3 + k * x

x = np.linspace(-1.2, 1.2, 1000)
abc = (x - 0.5)**2
efg = (x + 0.5)**2
Ep = k * abc * efg

# Plot the potential energy
plt.figure(figsize=(10, 6))
plt.plot(x, Ep, 'b-', label='Potential Energy')
plt.axhline(y=0.25, color='r', linestyle='--', label='E = 0.25 J')
plt.grid(True)
plt.xlabel('x (m)')
plt.ylabel('Ep (J)')
plt.title('Potential Energy Diagram')
plt.legend()

# Add points of interest
plt.plot(-0.5, 0, 'ko', label='Equilibrium point 1')
plt.plot(0.5, 0, 'ko', label='Equilibrium point 2')

plt.ylim(-0.1, 1)
plt.legend()
plt.show()

"""Se a energia for mais baixa do que 0.125J, vai oscilar na depresão do lado onde começou, ou à volta de -0.5m ou de 0,5m. 
   Se a energia for entre 0.125J e 0.25J,vai oscilar nos dois lados, com movimento mais devegar quando atravesa o centro."""
