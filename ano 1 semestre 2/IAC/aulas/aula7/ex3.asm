.data

prompt:	.asciiz "Introduza uma string\n"
result: .asciiz "\nO número de carateres numéricos: "
str: 	.space 40

.text
main: 	
	la 	$a0, prompt
	li 	$v0, 4
	syscall
	
	la 	$a0, str
	li 	$v0, 40
	li	$v0, 8
	syscall
	
	li 	$t1, 0	# n = 0 (contador de dígitos)
	li 	$t0, 0	# i = 0 (índice)
	la	$t3, str
	
for:	
	addu	$t2, $t3, $t0
	lb	$t4, 0($t2)
	beq	$t4, $0, endfor
	
	# Verifica se é um dígito
	blt	$t4, '0', not_digit
	bgt 	$t4, '9', not_digit
	addi	$t1, $t1, 1	# n++
	
not_digit:
	addi	$t0, $t0, 1	# i++
	j for
	
endfor:
	# Imprime a string result
    	la   $a0, result
    	li   $v0, 4
  	syscall

	# Imprime o número de dígitos
	move  $a0, $t1
	li    $v0, 1
	syscall

	# Exit
   	li   $v0, 10
   	syscall