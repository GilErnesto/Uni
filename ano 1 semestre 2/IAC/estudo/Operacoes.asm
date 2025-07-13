	.text
	li	$t1, 20
	li	$t2, 10
	add	$t3, $t2, $t1 #soma de t2 + t1 e fica no t3   30
	#sub	$t3, $t2, $t1 #subtrai de t2 - t1 e fica no t3	-10
	#mul	$t3, $t2, $t1 #multiplica de t2 * t1 e fica no t3  200
	#div	$t3, $t2, $t1 #divide de t2 / t1 e fica no t3   hi=2  lo=0		parte inteira (lo) resto (hi) usar mf(lo/hi) $s0 move o conteudo

	#OU

	#addi	$t3, t1, 10      É como o add, mas só é precios estar 1 valor registado
	#addi	$t3, t1, -10    É como o sub, mas só é precios estar 1 valor registado e outro negativo para subtrair
	#sll	$t3, t1, 2       Só funciona com multiplicaçoes base 2, aqui é 20 * 2^2
	#srl	$t3, t1, 2       Só funciona com divisao base 2, aqui é 20 / 2^2

	li 	$v0, 1
	move	$a0, $t3
	syscall

	li	$v0, 10
	syscall