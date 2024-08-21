.data
weight: .word 0
height: .word 0
bmi: .word 0

.text
li $v0, 5
syscall 
move $t0, $v0 #store v0 in t0

#
li $v0, 5
syscall
move $t1, $v0 # store v0 in t0

# h^2
mul $t2, $t1, $t1
div $t0, $t1
mflo $t3

sw $t3, bmi

li $v0, 10
syscall