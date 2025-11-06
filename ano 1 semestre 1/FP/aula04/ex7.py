i = 0
contador = 0

while True:
    n = input("Digite um número real -> ")
    if n == "":
        print(f"a tua média é: {média}")
        break
    n = int(n)
    i = i + n
    contador = contador + 1
    média = i / contador
