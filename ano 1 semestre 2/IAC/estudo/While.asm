		.data
msg:     	.asciiz 	"Valor de i: "

	.text

main:
    	li      	$t0, 0          # i = 0

while_loop:
    	bge     	$t0, 5, end_loop   # enquanto i < 5

    	# imprimir a mensagem
    	li      	$v0, 4
    	la      	$a0, msg
    	syscall

    	# imprimir valor de i
    	move    	$a0, $t0
    	li      	$v0, 1
    	syscall

    	# imprimir nova linha
    	li      	$v0, 11
    	li      	$a0, 10     # caractere '\n'
    	syscall

    	# incrementar i
    	addi    	$t0, $t0, 1
    	j       	while_loop

end_loop:
    	li      	$v0, 10      # sair
    	syscall
