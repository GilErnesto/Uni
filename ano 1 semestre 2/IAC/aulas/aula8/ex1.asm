.data

prompt1:	.asciiz	"Introduza um numero \n"         		# Mensagem para solicitar um número ao utilizador
result1:	.asciiz	"O fatorial do número inserido: " 	# Mensagem a ser exibida antes do resultado
result2:	.asciiz	" é: "

.text
main:
    la   $a0, prompt1       # Carrega o endereço da mensagem prompt1 em $a0
    li   $v0, 4             # Código da syscall 4 (imprimir string)
    syscall                 # Chamada de sistema: imprime "Introduza um numero"

    li   $v0, 5             # Código da syscall 5 (ler um inteiro)
    syscall                 # Chamada de sistema: lê o número do utilizador
    move $a0, $v0           # Move o número lido (em $v0) para $a0 (argumento da função factorial)
    la $s0, ($a0)

    jal factorial           # Chamada à função factorial (jump and link)

    la   $a0, result1        # Carrega o endereço da mensagem "O fatorial do número..." para $a0
    li   $v0, 4             # Código da syscall 4 (imprimir string)
    syscall                 # Imprime a mensagem

    la   $a0, ($s0)         # Carrega o endereço de $t0 para $a0 (espera-se o valor calculado) — NOTA: não está a aceder diretamente ao valor
    li   $v0, 1             # Código da syscall 1 (imprimir inteiro)
    syscall                 # Imprime o número armazenado em $t0 (fatorial calculado)

    la   $a0, result2        # Carrega o endereço da mensagem "O fatorial do número..." para $a0
    li   $v0, 4             # Código da syscall 4 (imprimir string)
    syscall                 # Imprime a mensagem
    
    la $a0, ($t0)
    li $v0, 1
    syscall

    li   $v0, 10            # Código da syscall 10 (terminar o programa)
    syscall                 # Termina o programa

# Função factorial:
# Calcula o fatorial do número dado em $a0
# Resultado final é guardado em $t0 (e também copiado para $v0)
factorial:
    li   $t0, 1             # Inicializa o acumulador de fatorial com 1 (t0 = 1)
    move $t1, $a0           # Copia o número original para $t1 (contador)

for_fact:
    ble  $t1, 0, endfor_fact  # Se t1 <= 0, termina o ciclo
    mul  $t0, $t0, $t1        # t0 = t0 * t1 (multiplica o acumulador pelo contador)
    subi $t1, $t1, 1          # Decrementa o contador: t1 = t1 - 1
    j for_fact                # Repete o ciclo

endfor_fact:
    move $v0, $t0           # Copia o resultado para $v0 (valor de retorno da função)
    jr   $ra                # Retorna da função para o endereço de retorno (armazenado em $ra)
