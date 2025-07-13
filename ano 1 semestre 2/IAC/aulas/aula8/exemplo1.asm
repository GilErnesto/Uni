	.text            # Início da secção de código

main:	
	li $a0, 2        # Carrega o valor 2 no registrador $a0 (argumento 1 da função)
	li $a1, 3        # Carrega o valor 3 no registrador $a1 (argumento 2 da função)
	
	jal sum          # Salta para a função 'sum' e guarda o endereço de retorno em $ra
	
	# Aqui o resultado da soma está agora em $v0

	li $v0, 10       # Código da syscall para terminar o programa (exit)
	syscall          # Chama o sistema e termina o programa

# Função: sum
# Entrada: $a0 e $a1
# Saída: resultado da soma em $v0
sum:	
	add $v0, $a0, $a1   # Soma os dois argumentos: $v0 = $a0 + $a1
	jr $ra              # Retorna para o endereço guardado em $ra (de volta ao main)
