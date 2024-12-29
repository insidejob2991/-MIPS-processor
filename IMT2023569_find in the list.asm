.data
array:  .word 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 6, 7, 8, 5, 5
array_size: .word 16
input_prompt: .asciiz "Enter a number: "
output_prompt: .asciiz "The number of occurrences of the input in the array is: "

.text
.globl main
main:
    la $t0, array
    li $t1, 0    # counter for number of occurrences
    li $t2, 0    # counter for array index
    # read input
    li $v0, 5
    syscall
    move $t3, $v0
    # load address of array_size
    la $t5, array_size
    lw $t6, 0($t5)
loop:
    bge $t2, $t6, print_result
    lw $t4, 0($t0)
    beq $t3, $t4, inc_counter
    addiu $t0, $t0, 4
    addiu $t2, $t2, 1
    j loop
inc_counter:
    addiu $t1, $t1, 1
    addiu $t0, $t0, 4
    addiu $t2, $t2, 1
    j loop

print_result:
    # print number of occurrences
    li $v0, 1
    move $a0, $t1
    syscall

    # end program
    li $v0, 10
    syscall
