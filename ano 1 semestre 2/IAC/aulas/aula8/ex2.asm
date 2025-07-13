	.data
prompt:	.asciiz "Texto:\n"
result: 	.asciiz "Nº de palavras: "

	.text
	
main:
	la   $a0, prompt  # Carrega o endereço da mensagem prompt1 em $a0
    	li   $v0, 4             	# Código da syscall 4 (imprimir string)
    	syscall                 	# Chamada de sistema: imprime "Introduza um numero"

    	li   $v0, 8             	# Código da syscall 8 (ler um str)
    	syscall                 	# Chamada de sistema: lê o número do utilizador
    	move $a0, $v0      # Move o str lido (em $v0) para $a0 (argumento da função)
    	
    	jal strlen
    	
strlen:
	li	$t0, 0	#n = 0
	li	$1, 0	#i = 0
	
while_strlen:

	addu 	$t2, $a0, $t0		# $t2 = endereço de str[i]
	ld		$t3, ($t2)
    	beq  	$t3, $zero, end_strlen

    	addi 	$t1, $t1, 1    # n++
    	addi 	$t0, $t0, 1    # i++
    	j    while_strlen

end_strlen:
    	move $v0, $t1       # retorna n em $v0
    	jr   $ra           	 	# retorna para o chamador