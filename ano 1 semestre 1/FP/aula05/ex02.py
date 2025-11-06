def inputFloatList():
    print("Digite um número para adicionar à lista ")
    print("Caso queira PARAR não escreva nada")
    while True:
        n = input("-> ")
        if n == "":
            # lst.remove('') se n for int não é preciso
            print(f"A tua lista é esta -> {lst}")
            break
        n = int(n)
        a = lst.append(n)
    return lst


def countLower(v):
    b = len(lst)
    for i in range(b):
        if int(lst[i]) < v:
            a = lst_v.append(lst[i])
            continue
    print(
        "Este são os números da lista que são menores que N:",
        ", ".join(map(str, lst_v)),
    )
    return lst_v


def minmax(nmax, nmin):
    nmin = nmax = lst[0]
    for item in lst:
        if nmin > item:
            nmin = item
        if nmax < item:
            nmax = item
    print(f"O valor máximo é {nmax} e o valor mínimo é {nmin}")
    return nmax + nmin


def medio():
    inputFloatList()
    nmin = nmax = lst[0]
    soma_min_max = int(minmax(nmax, nmin))
    medio = soma_min_max / 2
    print(f"O valor médio entre o mínimo e o máximo é {medio}")


def n4():
    inputFloatList()
    v = int(input("Digite um número -> "))
    countLower(v)
    nmin = nmax = 0
    minmax(nmax, nmin)


lst = []
lst_v = []
print("Escolhe uma das opções")
print(
    "1-> Fazer uma lista\n2-> Ver quais números são menores que N numa lista\n3-> Ver o Máximo e o Mínimo de uma lista\n4-> Fazer o 2 e o 3\n5-> Determine o valor médio entre o mínimo e o máximo e quantos números são inferiores a esse valor"
)
a = int(input("-> "))

if a == 1:
    inputFloatList()
elif a == 2:
    inputFloatList()
    lst_v = []
    v = int(input("Digite um número -> "))
    countLower(v)
elif a == 3:
    inputFloatList()
    nmin = nmax = 0
    minmax(nmax, nmin)
elif a == 4:
    n4()
else:
    medio()
