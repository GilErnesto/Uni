	.data
prompt: .asciiz "O conteudo do Array é: \n"  # Mensagem a imprimir antes do conteúdo do array
lista:  .word 4, 3, -2, 1, 27, 45            # Array de inteiros inicializado com 6 elementos

	.text
	.globl main

main: 
    	# Imprimir a string do prompt
    	la	$a0, prompt       # $a0 <- endereço da string "O conteudo do Array é: \n"
	li   	$v0, 4            # $v0 <- 4 (código da syscall para imprimir string)
	syscall                # Faz a system call para imprimir a string
	
	# Inicializações
	la   	$t2, lista        # $t2 <- endereço base do array lista[]
	li   	$t0, 0            # $t0 <- i = 0 (contador do loop)

for:
    	bge  	$t0, 6, enfor     # if (i >= 6) salta para enfor (fim do ciclo)

   	# Aceder ao elemento lista[i]
    	sll  	$t1, $t0, 2       # $t1 <- i * 4 (offset em bytes para acesso ao array)
    	add  	$t1, $t2, $t1     # $t1 <- endereço de lista[i]
    	lw   	$a0, 0($t1)       # $a0 <- valor de lista[i]
    
    	# Imprimir o valor inteiro
    	li   	$v0, 1            # $v0 <- 1 (código da syscall para imprimir inteiro)
    	syscall                # Faz a system call para imprimir o valor

    	# Incrementar o índice i
    	addi 	$t0, $t0, 1       # i++

    	j    	for               # Volta ao início do ciclo

enfor:
    	# Terminar o programa
    	li   	$v0, 10           # $v0 <- 10 (código da syscall para sair)
    	syscall                # Faz a system call para terminar
