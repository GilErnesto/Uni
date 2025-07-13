	.data
myArray:	
	.align	2	#0=byte   1= Char    2=int/Str    3=double
	.space	16	# 4 int como cada 1 ocupa 4 bytes = 16 bytres de array total

	.text
main:	
	move 	$t0, $zero
	move 	$t1, $zero
	li	$t2, 16

loop:
	beq	$t0, $t2, saiLoop
	sw	$t1, myArray($t0)
	addi	$t0, $t0, 4
	addi	$t1, $t1, 1
	j	loop

saiLoop:
	move 	$t0, $zero
	imprime:
		beq	$t0, $t2, end
		li	$v0, 1
		lw	$a0, myArray($t0)
		syscall

		addi $t0, $t0, 4
		j	imprime
	
end:
	li	$v0, 10
	syscall