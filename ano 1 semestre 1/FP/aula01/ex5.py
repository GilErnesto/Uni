# pedir as velocidades

v1 = float(input("Qual foi a velocidade que da primeira viagem? (Km/h) -> "))
v2 = float(input("Qual foi a velocidade que da segunda viagem? (Km/h) -> "))

# calculo

vm = 2 * v1 * v2 / (v1 + v2)

# prints

print(f"Sabendo que v1={v1}Km/h e v2={v2}/km/h")
print(f"A velocidade média das duas viagens é de {vm:.2f} Km/h")
