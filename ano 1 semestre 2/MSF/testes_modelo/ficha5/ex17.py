import numpy as np
import matplotlib.pyplot as plt
def maxminv(xm1,xm2,xm3,ym1,ym2,ym3):  
    # Máximo ou mínimo usando o polinómio de Lagrange
    # Dados (input): (x0,y0), (x1,y1) e (x2,y2) 
    # Resultados (output): xm, ymax 
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)

    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xm=0.5*xmla/(a+b+c)

    xta=xm-xm1
    xtb=xm-xm2
    xtc=xm-xm3

    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xm, ymax

m  = 0.25
k = 1
b = 0.1
x0 = 0.4

tf = 20
dt = 0.001
N = int(tf/dt)

x = np.zeros(N)
x[0] = x0
vx = np.zeros(N)
vx[0] = 0
t = np.zeros(N)
t[0] = 0

for i in range(N-1):
    Fx = -k * x[i] - b * vx[i]
    ace = Fx / m
    
    vx[i+1] = vx[i] + ace * dt
    x[i+1] = x[i] + vx[i+1] * dt 
    
    t[i+1] = t[i] + dt
    
plt.figure
plt.plot(t, x, 'b-')
plt.title('Lei do Movimento')
plt.xlabel('Tempo (s)')
plt.ylabel('Movimento (m)')
plt.show()

# Detecção de máximos e mínimos
# Arrays para guardar os resultados
maximos_t = []
maximos_x = []
minimos_t = []
minimos_x = []

# Procurar mudanças de sinal na velocidade para identificar máximos/mínimos locais
for i in range(1, N-1):
    # Se a velocidade mudar de positivo para negativo, temos um máximo
    if vx[i-1] > 0 and vx[i] <= 0:
        # Aplicar o método de Lagrange para encontrar o máximo exato
        # Usamos o ponto atual e os dois pontos adjacentes
        t_max, x_max = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        maximos_t.append(t_max)
        maximos_x.append(x_max)
    
    # Se a velocidade mudar de negativo para positivo, temos um mínimo
    elif vx[i-1] < 0 and vx[i] >= 0:
        # Aplicar o método de Lagrange para encontrar o mínimo exato
        t_min, x_min = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        minimos_t.append(t_min)
        minimos_x.append(x_min)

# Converter para arrays NumPy para facilitar o trabalho
maximos_t = np.array(maximos_t)
maximos_x = np.array(maximos_x)
minimos_t = np.array(minimos_t)
minimos_x = np.array(minimos_x)

# Imprimir os valores das amplitudes (máximos e mínimos)
print("Máximos locais:")
for i in range(len(maximos_t)):
    print(f"t = {maximos_t[i]:.3f} s, x = {maximos_x[i]:.5f} m")

print("\nMínimos locais:")
for i in range(len(minimos_t)):
    print(f"t = {minimos_t[i]:.3f} s, x = {minimos_x[i]:.5f} m")

# Calcular e plotar o decaimento da amplitude
if len(maximos_x) > 1:
    plt.figure(figsize=(8, 5))
    plt.plot(maximos_t, maximos_x, 'ro-', label='Máximos')
    plt.plot(minimos_t, abs(minimos_x), 'go-', label='|Mínimos|')
    plt.title('Decaimento da Amplitude')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude (m)')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    
plt.figure()
plt.plot(maximos_t, np.log(maximos_x), '-ro')
plt.show()

# Regressão linear manual com numpy
ln_A = np.log(maximos_x)
n = len(maximos_t)
xy_sum = np.sum(maximos_t * ln_A)
x_sum = np.sum(maximos_t)
y_sum = np.sum(ln_A)
x2_sum = np.sum(maximos_t**2)

# Cálculo do declive (a) e da ordenada na origem (b)
a = (n * xy_sum - x_sum * y_sum) / (n * x2_sum - x_sum**2)
b = (y_sum - a * x_sum) / n

# Cálculo dos erros
y_pred = a * maximos_t + b
residuos = ln_A - y_pred
SSE = np.sum(residuos**2)
MSE = SSE / (n - 2)  # Variância dos resíduos
std_err = np.sqrt(MSE * n / (n * x2_sum - x_sum**2))

# Coeficiente de determinação (R²)
SST = np.sum((ln_A - np.mean(ln_A))**2)
R2 = 1 - SSE / SST if SST != 0 else 0

# Coeficiente de correlação
R = np.sqrt(R2) * (1 if a > 0 else -1)

# Plotar a linha de ajuste
fit_line = a * maximos_t + b
plt.plot(maximos_t, fit_line, 'b-', label=f'Ajuste: ln(A) = {b:.4f} {a:.4f}t')

# Valor teórico
theoretical_slope = -b/(2*m)
plt.axline((0, b), slope=theoretical_slope, color='g', linestyle='--', 
           label=f'Teórico: -{b}/(2m) = {theoretical_slope:.4f}')

plt.title('Logaritmo da Amplitude vs Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('ln(Amplitude)')
plt.grid(True)
plt.legend()

# Exibir os resultados
print("\nResultados da regressão linear para ln(Amplitude) vs Tempo:")
print(f"Declive experimental: {a:.6f} ± {std_err:.6f}")
print(f"Declive teórico: {theoretical_slope:.6f}")
print(f"Interceção: {b:.6f}")
print(f"Coeficiente de correlação: {R:.6f}")
print(f"Coeficiente de determinação (R²): {R2:.6f}")

# Comparação com a teoria
erro_percentual = abs((a - theoretical_slope) / theoretical_slope) * 100
print(f"\nErro percentual relativamente ao valor teórico: {erro_percentual:.2f}%")

if abs(a - theoretical_slope) <= 2 * std_err:
    print("O declive experimental está de acordo com a teoria (dentro de 2 desvios padrão).")
else:
    print("O declive experimental não está de acordo com a teoria.")

plt.show()