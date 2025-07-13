	.data
in_idade:	.asciiz	"Qual é a tua idade? ->"
out_idade:	.asciiz	"AH! Tu tens estes anos "

	.text
main:
	li 	$v0, 4
	la	$a0, in_idade
	syscall
	
	li	$v0, 5	#O valor escrito fica em v0
	syscall

	move	$t0, $v0
	
	li	$v0, 4
	la	$a0, out_idade
	syscall
	
	li	$v0, 1
	move	$a0, $t0
	syscall