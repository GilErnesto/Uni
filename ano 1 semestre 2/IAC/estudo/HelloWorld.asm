	.data
str: 	.asciiz "Hello World! \n"
car:	.byte	'E'
idade:	.word	16

	.text
	li	$v0, 4
	la	$a0, str		#indicar  o endere�o que est� o str
	syscall

	li	$v0, 4
	la	$a0, car		#indicar  o endere�o que est� o car
	syscall

	li	$v0, 1
	li	$a0, 16		#ou lw	$a0, idade	
 	syscall
