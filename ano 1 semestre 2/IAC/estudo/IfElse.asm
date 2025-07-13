	.data
prompt1:	.asciiz "Introduza o primeiro n�mero: "
prompt2:    	.asciiz "Introduza o segundo n�mero: "
msg_eq:     	.asciiz "Os n�meros s�o iguais.\n"
msg_neq:    	.asciiz "Os n�meros s�o diferentes.\n"
msg_gt:     	.asciiz "O primeiro n�mero � maior.\n"
msg_lt:     	.asciiz "O segundo n�mero � maior.\n"

	.text

main:
    	# Pergunta 1� n�mero
    	li      	$v0, 4
    	la      	$a0, prompt1
    	syscall

    	li      	$v0, 5
    	syscall
    	move    	$t0, $v0        # $t0 = primeiro n�mero

    	# Pergunta 2� n�mero
    	li      	$v0, 4
    	la      	$a0, prompt2
    	syscall

    	li      	$v0, 5
    	syscall
    	move    	$t1, $v0        # $t1 = segundo n�mero

    	# Compara��es
    	beq     	$t0, $t1, iguais
    	bgt     	$t0, $t1, maior
    	blt     	$t0, $t1, menor

iguais:
    	li      	$v0, 4
    	la      	$a0, msg_eq
    	syscall
    	j   	fim

maior:
    	li      	$v0, 4
    	la      	$a0, msg_gt
    	syscall
    	j       	fim

menor:
    	li      	$v0, 4
    	la      	$a0, msg_lt
    	syscall

fim:
    	li      	$v0, 10
    	syscall