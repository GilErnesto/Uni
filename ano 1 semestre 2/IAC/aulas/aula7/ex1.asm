	.data
	
a: 	.word 	0xffffffa5
b: 	.word 	0x000003ab
c: 	.space 	4
	
	.text
	
	.globl main
main:
	. . .
	la $a0, a
	la $a1, b
	la $a3, c
	lw $t0, 0($a0)
	lw $t1, 0($a1)
	sll $t1, $t1, 2
	sub $t2, $t0, $t1
	sw $t2, 0($a3)
	...
	
	# 1.a)-  A variável 'c' tem armazenado = 0xFFFFF0F9
	# 1.b)-  c = -3847