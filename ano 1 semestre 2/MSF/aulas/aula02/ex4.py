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
    x = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
    y = np.array([9.676 , 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119])
    N = len(x)
    sum_x, sum_y, sum_x2, sum_y2, sum_xy = calculate_sums(x, y)
    m, b, r2, delta_m, delta_b = calculate_parameters(N, sum_x, sum_y, sum_x2, sum_y2, sum_xy)
    
    print('---SEM log---')
    print(f"m = {m:.3f} +- {delta_m:.3f}")
    print(f"b = {b:.3f} +- {delta_b:.3f}")
    print(f"r2 = {r2:.3f}")
    figure, axis = plt.subplots(2,2)
    axis[0,0].plot(x, y, marker='o', linestyle='-')
    axis[0,0].set_title('linear Sem log')
    axis[0,0].set_xlabel('tempo')
    axis[0,0].set_ylabel('mCi')
    axis[1,0].semilogy(x, y, marker='o', linestyle='-')
    axis[1,0].set_title('semilog')
    axis[1,0].set_xlabel('tempo')
    axis[1,0].set_ylabel('mCi')
    # Exponential law y = y0 * e^(lambda * t)
    y0 = y[0]
    lambda_ = m
    y_exp = y0 * np.exp(lambda_ * x)   
    axis[0,1].plot(x, y_exp, marker='o', linestyle='-')
    axis[0,1].set_title('Exponential Fit')
    axis[0,1].set_xlabel('tempo')
    axis[0,1].set_ylabel('mCi')

    plt.show()

if __name__ == "__main__":
    main()


