import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

k = 1 #N/m
m = 1 #kg

#a
x0 = 4
v0 = 0

Ec = 0 #v = 0
Ep = 1/2 * k * x0 ** 2
Et = Ec + Ep

'''b'''

# Time parameters
t = np.arange(0, 10, 0.1)  # 10 seconds with dt=0.1s

# Arrays for Euler method
x_euler = np.zeros(len(t))
v_euler = np.zeros(len(t))
E_euler = np.zeros(len(t))

# Arrays for Euler-Cromer method
x_cromer = np.zeros(len(t))
v_cromer = np.zeros(len(t))
E_cromer = np.zeros(len(t))

# Initial conditions
x_euler[0] = x_cromer[0] = x0
v_euler[0] = v_cromer[0] = v0

# Initial energies
E_euler[0] = 0.5*k*x0**2 + 0.5*m*v0**2
E_cromer[0] = E_euler[0]

# Time step
dt = t[1] - t[0]

# Numerical integration
for i in range(len(t)-1):
    # Euler method
    a_euler = -k*x_euler[i]/m
    v_euler[i+1] = v_euler[i] + a_euler*dt
    x_euler[i+1] = x_euler[i] + v_euler[i]*dt
    E_euler[i+1] = 0.5*k*x_euler[i+1]**2 + 0.5*m*v_euler[i+1]**2
    
    # Euler-Cromer method
    a_cromer = -k*x_cromer[i]/m
    v_cromer[i+1] = v_cromer[i] + a_cromer*dt
    x_cromer[i+1] = x_cromer[i] + v_cromer[i+1]*dt  # Note: using v[i+1]
    E_cromer[i+1] = 0.5*k*x_cromer[i+1]**2 + 0.5*m*v_cromer[i+1]**2

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, E_euler, 'b-', label='Euler')
plt.plot(t, E_cromer, 'r--', label='Euler-Cromer')
plt.axhline(y=E_euler[0], color='g', linestyle=':', label='Analytical')
plt.xlabel('Time (s)')
plt.ylabel('Total Energy (J)')
plt.title('Energy Conservation: Euler vs Euler-Cromer')
plt.legend()
plt.grid(True)
plt.show()

# Print final energies
print(f"Initial energy: {E_euler[0]:.3f} J")
print(f"Final energy (Euler): {E_euler[-1]:.3f} J")
print(f"Final energy (Euler-Cromer): {E_cromer[-1]:.3f} J")