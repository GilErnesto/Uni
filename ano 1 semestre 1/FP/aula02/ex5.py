# chamada
tcs = int(input("Tempo da sua chamada em segundos -> "))

# contas
minutos = tcs // 60
segundos = tcs % 60
preço_por_se = 0.06 / 30
preço_base = 0.12

# if else
if minutos > 1:
    preço_ao_seg = segundos * preço_por_se
    preço_ao_min = minutos * preço_por_se * 60
    preço = preço_ao_seg + preço_ao_min


# print final
preço_total = preço + preço_base
print(f"O preço da chamda foi de {preço_total:.2f} euros")
