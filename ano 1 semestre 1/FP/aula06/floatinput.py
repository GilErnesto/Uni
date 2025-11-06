import math

def floatInput(prompt, min=-math.inf, max=+math.inf):
    if min >= max:
        raise ValueError("O valor mínimo (min) não pode ser maior ou igual ao valor máximo (max).")

    while True:
        try:
            res = float(input(prompt))
            if min <= res <= max:
                return res
            else:
                print(f"Erro! O valor deve estar entre [{min}, {max}].")
        except ValueError:
            print("Erro! Por favor, insira um número válido.")

def main():
    print("a) Tente introduzir valores inválidos como 1/2 ou 3,1416.")
    v = floatInput("Valor? ")
    print("v:", v)

    print("b) Tente introduzir valores inválidos como 15%, 110 ou -1.")
    h = floatInput("Humidade (%)? ", 0, 100)
    print("h:", h)

    print("c) Tente introduzir valores inválidos como 23C ou -274.")
    t = floatInput("Temperatura (Celsius)? ", min=-273.15)
    print("t:", t)

    # d) O que acontece se descomentar isto?
    try:
        impossible = floatInput("Valor em [3, 0]? ", min=3, max=0)
    except ValueError as e:
        print(f"Erro ao tentar usar limites inválidos: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro: {e}")
