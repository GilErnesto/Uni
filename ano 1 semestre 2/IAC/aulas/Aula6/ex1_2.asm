	.data
prompt: .asciiz "Digite um ́número:\n"	#char prompt1[] = "Introduza um numero\n";
		
	.text
main:
	la 	$a0, prompt		#print_str( prompt1 );
	li 	$v0, 4
	syscall
	
	li 	$v0, 5			#a = read_int();
	syscall
	move 	$t0, $v0
	
	li	$t1, 0			#i=0
	
for:	slt	$t2, $t1, $t0		#i < a
	beq	$t2, $zero, endfor
	
	li	$a0, '-'
	li	$v0, 11
	syscall				#print_char( '-' )
	
	addi 	$t1, $t1, 1		# i++
	j for
	
endfor: li  $v0, 10          
    	syscall