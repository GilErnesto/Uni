	.data
str1:       .space      100
str2:       .asciiz     "Boas pessoal"
str3:       .asciiz     " tudo bem?"

	.text

main:
    	la      $a0, str1      
    	la      $a1, str2     
    	jal     strcopy       

    	la      $a0, str1      
    	la      $a1, str3      
    	jal     strcat  

    	li      $v0, 4
    	la      $a0, str1
    	syscall

    	li      $v0, 10
    	syscall

strcat:
    	addiu   $sp, $sp, -8
    	sw      $ra, 0($sp)
    	sw      $s0, 4($sp)
    	move    $s0, $a0

strcat_loop:
    	lb      $t0, 0($a0)
    	beq     $t0, $zero, strcat_callcopy
    	addiu   $a0, $a0, 1
    	j       strcat_loop

strcat_callcopy:
    	jal     strcopy
    	move    $v0, $s0

    	lw      $ra, 0($sp)
    	lw      $s0, 4($sp)
    	addiu   $sp, $sp, 8
    	jr      $ra

strcopy:
    	li      $t0, 0
    	move    $t1, $a1  

strcopy_loop:
    	lb      $t2, 0($t1)
    	beq     $t2, $zero, strcopy_end
    	addu    $t3, $a0, $t0
    	sb      $t2, 0($t3)
    	addi    $t0, $t0, 1
    	addi    $t1, $t1, 1
    	j       strcopy_loop

strcopy_end:
    	addu    $t3, $a0, $t0
    	sb      $zero, 0($t3)
    	move    $v0, $a0
    	jr      $ra
