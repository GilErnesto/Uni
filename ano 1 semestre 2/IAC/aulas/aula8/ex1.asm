.data

prompt1:	.asciiz	"Introduza um numero \n"         		# Mensagem para solicitar um n�mero ao utilizador
result1:	.asciiz	"O fatorial do n�mero inserido: " 	# Mensagem a ser exibida antes do resultado
result2:	.asciiz	" �: "

.text
main:
    la   $a0, prompt1       # Carrega o endere�o da mensagem prompt1 em $a0
    li   $v0, 4             # C�digo da syscall 4 (imprimir string)
    syscall                 # Chamada de sistema: imprime "Introduza um numero"

    li   $v0, 5             # C�digo da syscall 5 (ler um inteiro)
    syscall                 # Chamada de sistema: l� o n�mero do utilizador
    move $a0, $v0           # Move o n�mero lido (em $v0) para $a0 (argumento da fun��o factorial)
    la $s0, ($a0)

    jal factorial           # Chamada � fun��o factorial (jump and link)

    la   $a0, result1        # Carrega o endere�o da mensagem "O fatorial do n�mero..." para $a0
    li   $v0, 4             # C�digo da syscall 4 (imprimir string)
    syscall                 # Imprime a mensagem

    la   $a0, ($s0)         # Carrega o endere�o de $t0 para $a0 (espera-se o valor calculado) � NOTA: n�o est� a aceder diretamente ao valor
    li   $v0, 1             # C�digo da syscall 1 (imprimir inteiro)
    syscall                 # Imprime o n�mero armazenado em $t0 (fatorial calculado)

    la   $a0, result2        # Carrega o endere�o da mensagem "O fatorial do n�mero..." para $a0
    li   $v0, 4             # C�digo da syscall 4 (imprimir string)
    syscall                 # Imprime a mensagem
    
    la $a0, ($t0)
    li $v0, 1
    syscall

    li   $v0, 10            # C�digo da syscall 10 (terminar o programa)
    syscall                 # Termina o programa

# Fun��o factorial:
# Calcula o fatorial do n�mero dado em $a0
# Resultado final � guardado em $t0 (e tamb�m copiado para $v0)
factorial:
    li   $t0, 1             # Inicializa o acumulador de fatorial com 1 (t0 = 1)
    move $t1, $a0           # Copia o n�mero original para $t1 (contador)

for_fact:
    ble  $t1, 0, endfor_fact  # Se t1 <= 0, termina o ciclo
    mul  $t0, $t0, $t1        # t0 = t0 * t1 (multiplica o acumulador pelo contador)
    subi $t1, $t1, 1          # Decrementa o contador: t1 = t1 - 1
    j for_fact                # Repete o ciclo

endfor_fact:
    move $v0, $t0           # Copia o resultado para $v0 (valor de retorno da fun��o)
    jr   $ra                # Retorna da fun��o para o endere�o de retorno (armazenado em $ra)
