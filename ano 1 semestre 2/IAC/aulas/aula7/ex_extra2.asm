	.data

prompt:   .asciiz "Introduza os 6 números: \n"   # Mensagem de pedido de entrada

prompt1:  .asciiz "O conteudo do Array é: \n"   # Mensagem de saída antes de imprimir o array

simbolo:  .asciiz " - "                         # Símbolo separador entre os números ao imprimir

	.align 2

lista:    .space 24                             # Reserva espaço para 6 inteiros (6 x 4 bytes)

	.text
	.globl main

main:
    	la 	$a0, prompt          # Carrega a mensagem prompt no registrador $a0
    	li 	$v0, 4               # Código da syscall 4 (imprimir string)
    	syscall 		     # Executa a system call

    	la 	$t2, lista           # $t2 <- endereço base do array lista[]
    	li 	$t0, 0               # Inicializa i = 0 em $t0

# Ciclo para ler 6 números do utilizador
for:
    	bge 	$t0, 6, print       # Se i >= 6, salta para a parte de impressão

    	li 	$v0, 5               # Código da syscall 5 (ler inteiro)
    	syscall                 # Executa a leitura; valor lido fica em $v0

    	sll 	$t1, $t0, 2         # Calcula o offset: i * 4 (porque int = 4 bytes)
    	add 	$t1, $t2, $t1       # $t1 <- endereço de lista[i]
    	sw	$v0, 0($t1)          # Guarda o inteiro lido em lista[i]

    	addi 	$t0, $t0, 1        # i++
    	j for                   # Volta ao início do ciclo

# Impressão dos valores armazenados no array
print:
    	la 	$a0, prompt1         # Carrega a mensagem "O conteudo do Array é: "
    	li 	$v0, 4               # syscall 4 (imprimir string)
    	syscall

    	la 	$a2, lista           # $a2 <- endereço base do array
    	li 	$a1, 0               # i = 0 em $a1

# Ciclo para imprimir os 6 valores do array
for1:
    	bge 	$a1, 6, endfor      # Se i >= 6, termina o ciclo

    	sll 	$t1, $a1, 2         # Offset = i * 4
    	add 	$t1, $a2, $t1       # $t1 <- endereço de lista[i]
    	lw 	$a0, 0($t1)          # Carrega lista[i] para $a0
    	li 	$v0, 1               # syscall 1 (imprimir inteiro)
    	syscall

    	la 	$a0, simbolo         # Carrega string " - " para separar os números
    	li 	$v0, 4               # syscall 4 (imprimir string)
    	syscall

    	addi 	$a1, $a1, 1        # i++
    	j 	for1                  # Volta ao início do ciclo

# Termina o programa
endfor:
    	li 	$v0, 10              # syscall 10 (terminar programa)
    	syscall
