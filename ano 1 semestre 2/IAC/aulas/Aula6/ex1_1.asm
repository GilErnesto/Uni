#void main(void)
#{
#int a;
	.data
prompt: .asciiz	"Introduza um numero\n"		#char prompt1[] = "Introduza um numero\n";
strpar: .asciiz "O numero é par\n"		#char strpar[] = "O numero é par\n";
strimp: .asciiz "O numero é impar\n"		#char strimp[] = "O numero é impar\n";
 						#print_str( prompt1 );

	.text
main: 	la $a0, prompt	#a = read_int();
	li $v0, 4
	syscall
	
	li $v0, 5
	syscall
	move $s1, $v0
	
	andi $t1,$s1,1 #if ((a & 1) == 0){

if: 	bne $t1, $0,else
	la $a0, strpar
	li $v0, 4
	syscall		#print_str( strpar );
	j endif

else:	#else {
	la $a0, strimp
	li $v0, 4
	syscall 	#print_str( strimp );
	
endif:
	li $v0, 10
	syscall 	#exit(); //system call 10
#}