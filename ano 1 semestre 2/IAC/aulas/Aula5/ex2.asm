	.data
numero1: 
numero2:

	.text
	li $v0, 5 	# $v0 = 5 (syscall "read_int")
	syscall 	# read_int() (o valor lido é
			# devolvido no reg. $v0)
	move $t0, $v0	# $t0 = $v0 ( num = read_int() )
	