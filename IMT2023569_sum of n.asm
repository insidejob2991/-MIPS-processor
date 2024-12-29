.data
n:    .word 0    # memory location to store user input n
i:    .word 0    # i initialized to 0
sum:  .word 0    # memory location to store final result sum

.text
.globl main

main:
    # load base address
    lui $s0, 0x1001

    # read integer input
    li $v0, 5
    syscall
    sw $v0, n      # store the user input in location n

loop:
    # load n and i
    lw $t0, n
    lw $t1, i

    # compute n+1
    addi $t0, $t0, 1

    # check if i == n+1, if yes then exit loop
    beq $t1, $t0, exit

    # load sum, compute sum + i, and store sum
    lw $t3, sum
    add $t3, $t3, $t1
    sw $t3, sum

    # increment i and store it
    addi $t1, $t1, 1
    sw $t1, i

    # jump to loop
    j loop

exit:
    # load sum, print integer, and exit
    lw $t3, sum
    li $v0, 1
    add $a0, $t3, $zero
    syscall
    li $v0, 10
    syscall
