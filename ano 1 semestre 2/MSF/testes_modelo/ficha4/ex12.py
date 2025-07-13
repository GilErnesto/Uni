import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Function to integrate: x^4"""
    return x**4

def trapezoidal_rule(f, a, b, n):
    """Calculate integral using trapezoidal rule
    Parameters:
        f: function to integrate
        a, b: integration limits
        n: number of intervals
    """
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    integral = h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
    return integral

# Test with different step sizes
ns = [10, 20, 50, 100, 200, 500, 1000]
exact_value = 1/5  # Analytical result of integral of x^4 from 0 to 1

errors = []
steps = []

for n in ns:
    result = trapezoidal_rule(f, 0, 1, n)
    h = 1/n
    error = abs(result - exact_value)
    
    errors.append(error)
    steps.append(h)
    print(f"N = {n:4d}, h = {h:.6f}, Result = {result:.8f}, Error = {error:.8f}")

# Plot error vs step size in log-log scale
plt.figure(figsize=(8, 6))
plt.loglog(steps, errors, 'bo-', label='Numerical Error')
plt.loglog(steps, np.array(steps)**2, 'r--', label='h²')
plt.xlabel('Step size (h)')
plt.ylabel('Error')
plt.title('Trapezoidal Rule Error vs Step Size')
plt.grid(True)
plt.legend()
plt.show()