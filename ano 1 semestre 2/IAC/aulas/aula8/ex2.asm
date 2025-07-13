	.data
prompt:	.asciiz "Texto:\n"
result: 	.asciiz "N� de palavras: "

	.text
	
main:
	la   $a0, prompt  # Carrega o endere�o da mensagem prompt1 em $a0
    	li   $v0, 4             	# C�digo da syscall 4 (imprimir string)
    	syscall                 	# Chamada de sistema: imprime "Introduza um numero"

    	li   $v0, 8             	# C�digo da syscall 8 (ler um str)
    	syscall                 	# Chamada de sistema: l� o n�mero do utilizador
    	move $a0, $v0      # Move o str lido (em $v0) para $a0 (argumento da fun��o)
    	
    	jal strlen
    	
strlen:
	li	$t0, 0	#n = 0
	li	$1, 0	#i = 0
	
while_strlen:

	addu 	$t2, $a0, $t0		# $t2 = endere�o de str[i]
	ld		$t3, ($t2)
    	beq  	$t3, $zero, end_strlen

    	addi 	$t1, $t1, 1    # n++
    	addi 	$t0, $t0, 1    # i++
    	j    while_strlen

end_strlen:
    	move $v0, $t1       # retorna n em $v0
    	jr   $ra           	 	# retorna para o chamador