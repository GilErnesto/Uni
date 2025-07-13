.data
prompt: .asciiz "Introduza um numero:\n"         # Mensagem para o usuário
result: .asciiz "O fatorial do numero inserido e: "  # Mensagem de resultado
msg:    .asciiz "O resultado nao e valido porque deu overflow\n"  # Mensagem de overflow

.text
main:
    # Mostra o prompt
    la $a0, prompt         # Carrega o endereço da mensagem "prompt"
    li $v0, 4              # Chamada para imprimir string (syscall 4)
    syscall                # Executa a chamada de sistema

    # Lê o número do usuário
    li $v0, 5              # Chamada para ler inteiro (syscall 5)
    syscall                # Executa a chamada de sistema
    move $t0, $v0          # Armazena o número lido em $t0 (n)

    # Inicializa valores para o cálculo do fatorial
    li $s0, 1              # $s0 = fatorial inicializado como 1 (f = 1)
    
for:
    # Verifica se i <= 0 (fim do loop)
    ble $t0, 0, endfor     # Se $t0 <= 0, sai do loop

    # Multiplica fatorial (f *= i)
    mult $s0, $t0          # HI, LO = $s0 * $t0
    mflo $s0               # Move o resultado da multiplicação (LO) para $s0
    mfhi $t1               # Move o valor de HI para $t1 (verificar overflow)

    # Verifica se houve overflow (HI != 0)
    bne $t1, $zero, overflow # Se HI != 0, vai para "overflow"

    # Decrementa i (i--)
    addi $t0, $t0, -1      # $t0 = $t0 - 1
    j for                  # Volta ao início do loop

overflow:
    # Mensagem de erro de overflow
    la $a0, msg            # Carrega o endereço da mensagem "msg"
    li $v0, 4              # Chamada para imprimir string (syscall 4)
    syscall                # Executa a chamada de sistema
    j exit_program         # Sai do programa

endfor:
    # Mostra a mensagem de resultado
    la $a0, result         # Carrega o endereço da mensagem "result"
    li $v0, 4              # Chamada para imprimir string (syscall 4)
    syscall                # Executa a chamada de sistema

    # Exibe o valor do fatorial
    move $a0, $s0          # Move o valor do fatorial para $a0
    li $v0, 1              # Chamada para imprimir inteiro (syscall 1)
    syscall                # Executa a chamada de sistema

exit_program:
    # Finaliza o programa
    li $v0, 10             # Chamada para encerrar programa (syscall 10)
    syscall                # Executa a chamada de sistema