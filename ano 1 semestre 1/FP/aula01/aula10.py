hora_i = 6 * 60 + 52
andar = 10
correr = 6 * 3
voltar = 10 * ( 1 + 3 )
hora_f = hora_i + (andar + correr + voltar)
horas = hora_f / 60
minutos = hora_f % 60

print(hora_f)
print(f'horas de chegada-> {horas:.0f}:{minutos:.0f}')
