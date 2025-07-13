	.data
.text

main:...
exit

x_to_y:

if:	
	bne	$a1, 0, endif
	li	$v0, 1
	jr	$ra

endif:
	subi	$a1, $a1, 1
	
	addiu	$sp, $sp, -8
	sw	$ra, 0($sp)
	sw	$a0, 4($sp)
	
