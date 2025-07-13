import numpy as np
import matplotlib.pyplot as plt

def calculate_acceleration(state, params):
    """
    Calculate the acceleration for the system.
    To be implemented for specific systems.
    
    Parameters:
    - state: A tuple (x, y, vx, vy) representing the state of the system.
    - params: A dictionary of system-specific parameters.
    
    Returns:
    - ax, ay: Accelerations in the x and y directions.
    """
    raise NotImplementedError("Define this function for your specific system.")

def euler_method(initial_state, t0, tf, dt, acceleration_func, params):
    """
    General Euler method for numerical integration.
    
    Parameters:
    - initial_state: A tuple (x0, y0, vx0, vy0) representing the initial state.
    - t0: Initial time.
    - tf: Final time.
    - dt: Time step.
    - acceleration_func: Function to calculate acceleration (e.g., gravitational force).
    - params: Dictionary of parameters required by the acceleration function.
    
    Returns:
    - t: Array of time values.
    - x, y: Arrays of position values.
    - vx, vy: Arrays of velocity values.
    """
    N = int((tf - t0) / dt)
    
    # Initialize arrays
    x = np.zeros(N)
    y = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)
    t = np.zeros(N)
    
    # Set initial conditions
    x[0], y[0], vx[0], vy[0] = initial_state
    t[0] = t0
    
    # Perform Euler integration
    for i in range(N - 1):
        ax, ay = acceleration_func((x[i], y[i], vx[i], vy[i]), params)
        
        vx[i + 1] = vx[i] + ax * dt
        vy[i + 1] = vy[i] + ay * dt
        
        x[i + 1] = x[i] + vx[i] * dt
        y[i + 1] = y[i] + vy[i] * dt
        
        t[i + 1] = t[i] + dt
    
    return t, x, y, vx, vy


# Parameters for the orbital motion
params = {
    'G': 4 * np.pi**2,  # Gravitational constant (AU^3/year^2/M_sun)
    'M': 1              # Mass of the Sun in solar masses
}
initial_state = (1.0, 0.0, 0.0, 2.0 * np.pi)  # (x0, y0, vx0, vy0)
t0, tf, dt = 0, 5, 0.001  # Time parameters

# Run simulation
t, x, y, vx, vy = euler_method(initial_state, t0, tf, dt, gravitational_acceleration, params)


    
'''...........................-----------------------------------------------------.........................................'''

import numpy as np
import matplotlib.pyplot as plt

def calculate_acceleration(state, params):
    """
    Calculate the acceleration for the system.
    To be implemented for specific systems.
    
    Parameters:
    - state: A tuple (x, y, vx, vy) representing the state of the system.
    - params: A dictionary of system-specific parameters.
    
    Returns:
    - ax, ay: Accelerations in the x and y directions.
    """
    raise NotImplementedError("Define this function for your specific system.")

def euler_method_without_time(initial_state, steps, step_size, acceleration_func, params):
    """
    General Euler method for numerical integration without explicit time.
    
    Parameters:
    - initial_state: A tuple (x0, y0, vx0, vy0) representing the initial state.
    - steps: Number of steps to iterate.
    - step_size: Step size for the iteration (h).
    - acceleration_func: Function to calculate acceleration (e.g., based on system dynamics).
    - params: Dictionary of parameters required by the acceleration function.
    
    Returns:
    - s: Array of step indices (or pseudo-time values).
    - x, y: Arrays of position values.
    - vx, vy: Arrays of velocity values.
    """
    # Initialize arrays
    x = np.zeros(steps)
    y = np.zeros(steps)
    vx = np.zeros(steps)
    vy = np.zeros(steps)
    s = np.arange(steps) * step_size  # Pseudo-step values for plotting
    
    # Set initial conditions
    x[0], y[0], vx[0], vy[0] = initial_state
    
    # Perform Euler integration
    for i in range(steps - 1):
        ax, ay = acceleration_func((x[i], y[i], vx[i], vy[i]), params)
        
        vx[i + 1] = vx[i] + ax * step_size
        vy[i + 1] = vy[i] + ay * step_size
        
        x[i + 1] = x[i] + vx[i] * step_size
        y[i + 1] = y[i] + vy[i] * step_size
    
    return s, x, y, vx, vy

# Example usage for a system without explicit time
def simple_harmonic_acceleration(state, params):
    """
    Calculate acceleration for a simple harmonic oscillator.
    
    Parameters:
    - state: A tuple (x, y, vx, vy) representing the state of the system.
    - params: Dictionary containing 'k' (spring constant) and 'm' (mass).
    
    Returns:
    - ax, ay: Accelerations in the x and y directions.
    """
    x, y, vx, vy = state
    k, m = params['k'], params['m']
    ax = -k * x / m  # Hooke's Law: F = -kx
    ay = -k * y / m  # If in 2D (you can adjust it for 1D systems)
    return ax, ay


# Parameters for the simple harmonic oscillator
params = {
    'k': 1.0,  # Spring constant
    'm': 1.0   # Mass
}
initial_state = (1.0, 0.0, 0.0, 0.0)  # (x0, y0, vx0, vy0)
steps = 500
step_size = 0.1  # Step size (can represent pseudo-time)

# Run simulation
s, x, y, vx, vy = euler_method_without_time(initial_state, steps, step_size, simple_harmonic_acceleration, params)