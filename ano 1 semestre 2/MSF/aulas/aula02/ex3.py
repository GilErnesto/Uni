import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def calculate_sums(x, y):
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_y2 = np.sum(y**2)
    sum_xy = np.sum(x*y)
    return sum_x, sum_y, sum_x2, sum_y2, sum_xy

def calculate_parameters(N, sum_x, sum_y, sum_x2, sum_y2, sum_xy):
    m = (N*sum_xy - sum_x*sum_y)/(N*sum_x2 - sum_x**2)
    b = (sum_y*sum_x2 - sum_x*sum_xy)/(N*sum_x2 - sum_x**2)
    r2 = ((N*sum_xy - sum_x*sum_y)**2)/((N*sum_x2 - sum_x**2)*(N*sum_y2 - sum_y**2))
    delta_m = abs(m)*np.sqrt((1-r2)/(N-2))
    delta_b = delta_m*(np.sqrt(sum_x2/N))
    return m, b, r2, delta_m, delta_b

def main():
    #array
    x = np.array([200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0])
    y = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])
    N = len(x)
    sum_x, sum_y, sum_x2, sum_y2, sum_xy = calculate_sums(x, y)
    m, b, r2, delta_m, delta_b = calculate_parameters(N, sum_x, sum_y, sum_x2, sum_y2, sum_xy)
    
    print('---SEM log---')
    print(f"m = {m:.3f} +- {delta_m:.3f}")
    print(f"b = {b:.3f} +- {delta_b:.3f}")
    print(f"r2 = {r2:.3f}")
    figure, axis = plt.subplots(2,2)
    axis[0,0].plot(x, y, marker='o', linestyle='-')
    axis[0,1].semilogy(x, y, marker='o', linestyle='-')
    axis[1,0].loglog(x, y, marker='o', linestyle='-')
    log_x = np.log(x)
    log_y = np.log(y)
    sum_x, sum_y, sum_x2, sum_y2, sum_xy = calculate_sums(log_x, log_y)
    m, b, r2, delta_m, delta_b = calculate_parameters(N, sum_x, sum_y, sum_x2, sum_y2, sum_xy)
    print('---COM log---')
    print(f"m = {m:.3f} +- {delta_m:.3f}")
    print(f"b = {b:.3f} +- {delta_b:.3f}")
    print(f"r2 = {r2:.3f}")
    axis[1, 1].plot(y, x**N, marker='o', linestyle='-')
    plt.title('Lei de potência')
    plt.xlabel('T (K)')
    plt.ylabel('E (J)')
    plt.show()

if __name__ == "__main__":
    main()


