	.data
prompt: 	.asciiz "Introduza os 6 números:\n"
prompt1:	.asciiz "O conteúdo do array é:\n"
separador:  	.asciiz " - "
	.align 2
lista:	.space 24       # 6 inteiros (6 × 4 bytes)

	.text
	.globl main

main:
	#Imprime o pedido de entrada
	la	$a0, prompt
	li	$v0, 4
	syscall

	# Lê os 6 números
	la	$t2, lista           # endereço base do array
	li	$t0, 0               # contador i = 0

read_loop:
	bge	$t0, 6, bubble_sort
	li	$v0, 5               # syscall: read_int
	syscall
	sll	$t1, $t0, 2
	add	$t1, $t2, $t1
	sw	$v0, 0($t1)
	addi	$t0, $t0, 1
	j read_loop

# Bubble Sort
bubble_sort:
    	li 	$s0, 1               # houveTroca = 1 (TRUE)

sort_outer:
    	beqz 	$s0, print         # enquanto houveTroca != 0
    	li 	$s0, 0               # houveTroca = 0
    	li 	$t0, 0               # i = 0

sort_inner:
    	li 	$t7, 5               # SIZE - 1 = 5
    	bge 	$t0, $t7, sort_outer

    	sll 	$t1, $t0, 2         # offset = i * 4
    	add 	$t3, $t2, $t1       # endereço de lista[i]
    	lw 	$t4, 0($t3)          # lista[i]
    	lw 	$t5, 4($t3)          # lista[i+1]

    	ble 	$t4, $t5, no_swap   # se lista[i] <= lista[i+1], salta

    # troca (swap)
    	sw 	$t5, 0($t3)
    	sw 	$t4, 4($t3)
    	li 	$s0, 1               # houveTroca = 1

no_swap:
    	addi 	$t0, $t0, 1
    	j sort_inner

# prints
print:
    	la 	$a0, prompt1
    	li 	$v0, 4
    	syscall

    	li 	$t0, 0
print_loop:
    	bge 	$t0, 6, end

    	sll 	$t1, $t0, 2
    	add 	$t1, $t2, $t1
    	lw 	$a0, 0($t1)
    	li 	$v0, 1
    	syscall

    	li 	$t6, 5
    	beq 	$t0, $t6, skip_sep  # não imprime "-" após o último número

    	la 	$a0, separador
    	li 	$v0, 4
    	syscall

skip_sep:
    	addi 	$t0, $t0, 1
    	j print_loop

# Termina o programa
end:
    	li 	$v0, 10
    	syscall
