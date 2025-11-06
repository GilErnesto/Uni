def lista(n):
    i = 1
    lista = 0
    for a in range(n):
        primo = n % i
        if primo == 0:
            lista = lista + i
        i += 1
    return lista


def categoria(lista, n):
    categoria = lista - n
    if categoria < n:
        return "Número Deficiente"
    elif categoria == n:
        return "Número Perfeito"
    else:
        return "Número Abundante"


n = int(input("n? -> "))
lista_c = lista(n)
print(categoria(lista_c, n))
