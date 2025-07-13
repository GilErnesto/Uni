	.data	
breakLine:	.asciiz	"\n"
max:	.asciiz	"max: "

	.text			# n = t0      m = t1      t = t2

main:				#int main(void)
				#{
				#int n,m,t;
	li 	$v0, 5		#n = read_int(); // syscall
	syscall

	move 	$t0, $v0
	move 	$t1, $t0		#m = n;

	move 	$t2, $t0		#t = n
for:
	ble	$t2, 1,  end	#t <=1

	li	$v0, 1		#print_int10(t); // syscall
	move	$a0, $t2
	syscall

	li	$v0, 4		#print_string("\n"); // syscall
	la	$a0, breakLine
	syscall

if_1:	
	andi 	$t4, $t2, 1	#(t & 1)
	beq	$t4, $zero, endfor	#(t & 1) == 0)  salta
	
	mul	$t2, $t2, 3	#t = 3 * t + 1
	addi	$t2, $t2, 1
if_2:
	ble	$t2, $t1, endfor	#if(t <= m
	move	$t1, $t2		#m = t

endfor:
	srl	$t2, $t2, 1	#t >>= 1
	j	for

end:
	li	$v0, 4		#print_string("max:"); // syscall
	la	$a0, max
	syscall

	li	$v0, 1		#print_int10(m) // syscall;
	move 	$a0, $t1
	syscall
	
	li	$v0, 4		#print_string("\n") // syscall;
	la	$a0, breakLine
	syscall			

	li	$v0, 10
	syscall