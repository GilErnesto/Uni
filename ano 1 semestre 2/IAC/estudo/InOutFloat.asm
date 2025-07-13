	.data
input:	.asciiz	"Qual o valor (float)? -> "
output:	.asciiz	"O seu valor é: "
#zero:	.float 	0.0

	.text
	li	$v0, 4
	la	$a0, input
	syscall

	li	$v0, 6	#O valor lido vai para $f0
	syscall
	
	li	$v0, 4
	la	$a0, output
	syscall
	
	mov.s	$f12, $f0		#para Double é mov.d e sycall é 3 e 7
	#lwc1	$f1, zero
	#add.s 	$f12, $f0, $f1

	li 	$v0, 2
	syscall

	li		$v0, 10
	syscall