import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 2000  # kg
g = 9.81  # m/s^2
theta = np.radians(5)  # angle in radians
mu = 0.04  # rolling resistance coefficient
Cres = 0.25  # air resistance coefficient
A = 2  # frontal area in m^2
rho = 1.225  # air density in kg/m^3
P_up = 40000  # power uphill in W
P_down = -15000  # power downhill in W
distance = 2000  # target distance in m

def calculate_forces(v, power):
    # Gravity force
    Fg = -m*g*np.sin(theta)
    
    # Rolling resistance
    Fr = -mu*m*g*np.cos(theta)
    
    # Air resistance
    Fa = -0.5*Cres*A*rho*abs(v)*v
    
    # Motor force (P = F*v)
    Fm = power/v if abs(v) > 0.01 else 0
    
    return Fg + Fr + Fa + Fm

def simulate_motion(v0, power, dt=0.01, max_t=1000):
    # Arrays for time, position, velocity
    t = [0]
    x = [0]
    v = [v0]
    
    while x[-1] < distance and t[-1] < max_t:
        # Calculate acceleration
        a = calculate_forces(v[-1], power)/m
        
        # Update velocity and position
        v_new = v[-1] + a*dt
        x_new = x[-1] + v[-1]*dt
        
        t.append(t[-1] + dt)
        v.append(v_new)
        x.append(x_new)
    
    return np.array(t), np.array(x), np.array(v)

# Uphill simulation
t_up, x_up, v_up = simulate_motion(1, P_up)

# Downhill simulation
t_down, x_down, v_down = simulate_motion(20, P_down)

# Calculate work done
def calculate_work(t, v, power):
    return np.trapz(np.full_like(t, power), t)

W_up = calculate_work(t_up, v_up, P_up)
W_down = calculate_work(t_down, v_down, P_down)

# Energy balance with 50% regenerative braking efficiency
energy_difference = W_up + 0.5*W_down

# Print results
print(f"Uphill journey:")
print(f"Time taken: {t_up[-1]:.1f} s")
print(f"Work done: {W_up/1000:.1f} kJ")

print(f"\nDownhill journey:")
print(f"Time taken: {t_down[-1]:.1f} s")
print(f"Work done: {W_down/1000:.1f} kJ")

print(f"\nNet energy consumed: {energy_difference/1000:.1f} kJ")

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t_up, x_up, 'b-', label='Uphill')
plt.plot(t_down, x_down, 'r-', label='Downhill')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t_up, v_up, 'b-', label='Uphill')
plt.plot(t_down, v_down, 'r-', label='Downhill')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()