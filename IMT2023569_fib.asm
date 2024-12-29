.data
    .align 2
    input_num:      .word 0       # Memory location to store input_num
    .align 2
    a:      .word 0       # Memory location for variable a, initialized to 0    
    .align 2
    b:      .word 1       # Memory location for variable b, initialized to 1   
    .align 2
    c:      .word 1       # Memory location for variable c, initialized to 1
    .align 2
    iterator:      .word 0       # iterator iterator initialized to  
    .align 2
    ans:    .word 0       # Memory location for int ans                
    
.text
    .globl main
    
main:
    lui $s0, 0x1001
    
    li $v0, 5                  # System call code for reading integer
    syscall
    sw $v0, 0($s0)             # Store the user input in location input_num
    
loop:
    
    lw $s1, 16($s0)           
    lw $s2, 0($s0)
    beq $s1, $s2, exit       # if iterator==input_num -> branch to exit
    
    lw $s3, 4($s0)
    lw $s4, 8($s0)
    lw $s5, 12($s0)
    sw $s4, 4($s0)           # a = b
    sw $s5, 8($s0)           # b = c
    add $s6, $s4, $s5     
    sw $s6, 12($s0)          # c = a+b  
    addi $s1, $s1, 1         # iterator++
    sw $s1, 16($s0)
    
    j loop                   # go to loop again
exit:
    lw $s7, 4($s0)            
    sw $s7, 20($s0)          # storing the returned value(a) in ans
    
    li  $v0, 1               # System call code for printing integer
    add $a0, $s7, $zero  
    syscall
     
    li $v0, 10               # System call to exit
    syscall