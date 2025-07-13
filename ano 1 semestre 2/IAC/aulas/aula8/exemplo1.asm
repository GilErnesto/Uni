	.text            # In�cio da sec��o de c�digo

main:	
	li $a0, 2        # Carrega o valor 2 no registrador $a0 (argumento 1 da fun��o)
	li $a1, 3        # Carrega o valor 3 no registrador $a1 (argumento 2 da fun��o)
	
	jal sum          # Salta para a fun��o 'sum' e guarda o endere�o de retorno em $ra
	
	# Aqui o resultado da soma est� agora em $v0

	li $v0, 10       # C�digo da syscall para terminar o programa (exit)
	syscall          # Chama o sistema e termina o programa

# Fun��o: sum
# Entrada: $a0 e $a1
# Sa�da: resultado da soma em $v0
sum:	
	add $v0, $a0, $a1   # Soma os dois argumentos: $v0 = $a0 + $a1
	jr $ra              # Retorna para o endere�o guardado em $ra (de volta ao main)
