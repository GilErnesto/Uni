import math

# pedir os lados
print("Sabendo que o lado A é o adejacente e o B o oposto")

la = float(input("Comprimento de A em cm ->"))
lb = float(input("Comprimento de B em cm ->"))

# calcular a hip
lc = math.sqrt(la**2 + lb**2)

# calcular o angulo e converter
angulor = math.acos(la / lc)
angulog = math.degrees(angulor)

# print
print(f"A hipotenusa = {lc:.2f} cm e o angulo entre A e C = {angulog:.2f}º")
