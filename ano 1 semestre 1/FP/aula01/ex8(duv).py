# saber os Moradores e os Andares
A = int(input("Quantos andares tem o prédio? (conta o R/C) -> "))
M = int(input("Quantos moradores tem o prédio? -> "))


#qual é a PA para este caso??? problema matemático



# calculo
uso = M * 4  # quantas vezes o elevaodr é usado no dia
h = A * 3  # altura do prédio

dt_dia = h * uso  # distância que o elevador 'anda' por dia: uso x h
# tempo que o elevador 'anda' por dia (1m/s): d_dia = t_dia
dt_ano = dt_dia * 365

d_ano_km = dt_ano / 1000
t_ano_h = dt_ano / 3600

# prints
print(f"O elevador faz {d_ano_km}Km e {t_ano_h}H por ano")
