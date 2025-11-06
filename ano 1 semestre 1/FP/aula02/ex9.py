ctp = float(input("Qual o valor do CTP? "))
ct = float(input("Qual o valor do CT? "))

nota_tp = ctp * 0.3
nota_t = ct * 0.7
nf = nota_tp + nota_t

if ctp < 6.5 or ct < 6.5:
    print("código 66: aluno reprovado por nota mínima")
    atpr = float(input("Qual é o valor do ATPR? "))
    apr = float(input("Qual é o valor do APR? "))
    if ctp < atpr:
        nota_tp = atpr
    else:
        nota_tp = ctp
    if ct < apr:
        nota_p = apr
    else:
        nota_p = ct

print(f"A nota final é de {nf} valores")
