	.data
input:	.asciiz	"Qual é o teu nome -> "
output:	.asciiz	"Boas,  "
nome:	.space 	30

	.text
main:
	li 	$v0, 4
	la	$a0, input
	syscall
	
	li	$v0, 8
	la	$a0, nome
	la	$a1, 30
	syscall
	
	li	$v0, 4
	la	$a0, output
	syscall
	
	li	$v0, 4
	la	$a0, nome
	syscall