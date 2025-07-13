	.data		#void main(void)
						#{
minus:	.asciiz	"texto em minusculas" 		#static char minus[] = "texto em minusculas" ;
maius:	.space	20				#static char maius[20];
		
	.text
main: 	
	li	$t0, 0		#int i=0;
	la	$t1, minus	# t1 =  end inicial de minus - minus [0]
				#{
while:	
	addu	$t2, $t1, $t0	#t2 = minus + i * 1 = minus[i]	
	lb	$t3, 0($t2)	#t3 = cópia de minus[i]
	beq	$t3, '\0', endwhile	#while( minus[i] != ‘\0’)

if:	
	li   	$t6, 'a'
    	li   	$t7, 'z'
    	blt  	$t3, $t6, skip     # if (t3 < 'a') skip conversão
    	bgt  	$t3, $t7, skip     # if (t3 > 'z') skip conversão
    	addi	$t3, $t3, -32    	# converte para maiúscula

skip:
	la	$t4, maius	
	addu	$t5, $t4, $t0	#t5 = maius + i*1 = minus[i]
	sb	$t3, 0($t5)	#maius[i] = t3
	addi 	$t0, $t0, 1 	#i++
	j while

#}


endwhile:
	# Imprime a string maius
    	la   $a0, maius
    	li   $v0, 4
  	syscall

	# Exit
   	li   $v0, 10
   	syscall