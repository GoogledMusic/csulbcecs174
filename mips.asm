.data
	message:	.asciiz"Hello everyone.\nMy name is Brandon.\n"
.text
	main:
		jal displayMessage
		
		addi $s0, $zero, 20
		
		#Print number 5 to the screen
		li $v0, 1
		add $a0, $zero, $s0
		syscall
	
	# Tell the system that the program is done
	li $v0, 10
	syscall
	
	displayMessage:
		li $v0, 4
		la $a0, message
		syscall
		
		jr $ra