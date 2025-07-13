	.data
str: .asciiz "Olá Mundo"

	.text
	la	$a0, str
	li	$v0, 4
	syscall
	#comentário
	