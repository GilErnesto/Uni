	.data
prompt1:	.asciiz "Introduza o primeiro número: "
prompt2:    	.asciiz "Introduza o segundo número: "
msg_eq:     	.asciiz "Os números são iguais.\n"
msg_neq:    	.asciiz "Os números são diferentes.\n"
msg_gt:     	.asciiz "O primeiro número é maior.\n"
msg_lt:     	.asciiz "O segundo número é maior.\n"

	.text

main:
    	# Pergunta 1º número
    	li      	$v0, 4
    	la      	$a0, prompt1
    	syscall

    	li      	$v0, 5
    	syscall
    	move    	$t0, $v0        # $t0 = primeiro número

    	# Pergunta 2º número
    	li      	$v0, 4
    	la      	$a0, prompt2
    	syscall

    	li      	$v0, 5
    	syscall
    	move    	$t1, $v0        # $t1 = segundo número

    	# Comparações
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