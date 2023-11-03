; Encrypts a string using a Caesar cipher.
; CSC 225, Assignment 3
; Given code, Winter '20

; TODO: Complete this program.

       .ORIG x3000         ; Start at x3000.
       AND R1, R1, #0      ; Reset R1
       AND R2, R2, #0      ; Reset R2
       AND R3, R3, #0      ; Reset R3
       AND R4, R4, #0      ; Reset R4
       AND R5, R5, #0      ; Reset R5
       AND R6, R6, #0      ; Reset R6
       AND R7, R7, #0      ; Reset R7
       LEA R0, KEY         ; Loads user key prompt into R0
       PUTS                ; Prints from R0
       GETC                ; Read the character.
       OUT                 ; Prints out the character so user can see what they've typed
       LD R1, CONVERSION   ; Load ASCII conversion factor -48 into R1.
       ADD R2, R1, R0      ; Add to convert to ASCII
       
       LOOPZ GETC
       ADD R0, R0, #-10
       BRnp LOOPZ
       
       LEA R0, STRING      ; Loads character into R0. 
       PUTS                ; Prompts input message from user.
       LEA R3, INPUT       ; Saves the memory address in R3.
       
LOOP1 GETC                 ; Reads the char
       OUT                 ; Print out the character
       STR R0, R3, #0      ; Store the character into memory address in R3
       ADD R3, R3, #1      ; Increment the memory address by 1
       ADD R0, R0, #-10    ; Checks if Enter key was hit
       BRnp LOOP1          ; Break out of loop if Enter Key was hit

       LEA R3, INPUT       ; Saves address of input into R3 and R7 and R6
       LEA R7, INPUT
       LEA R6, INPUT
       LDR R0, R3, #0      ; Load value from address in R3 into R0
       
LOOP2   AND R1, R1, #0      ; Reset R1
       ADD R0, R0, R2
       STR R0, R3, #0      ; Stores char from address in R3 into R0
       ADD R3, R3, #1      ; Increment R3
       LDR R0, R3, #0      ; Load value from address into R0
       BRnp LOOP2           ; While loop for not zero
       
       LEA R0, RETURN      ; Loads char into R0.
       PUTS                ; Prints R0
       ADD R3, R3, #-1     ; Iterate through R3
       AND R0, R0, #0      ; Reset R0
       STR R0, R3, #0      ; Stores to address in R3
       LEA R0, INPUT       ; Loads INPUT address into R0
       PUTS                ; Prints the string

       HALT                ; Halt.

CONVERSION   .FILL xFFD0   ; #-48
KEY .STRINGZ "Encryption key (0-9): "
STRING .STRINGZ "\nUnencrypted string: "
RETURN .STRINGZ "Encrypted string: " 
INPUT   .BLKW #32          ; Reserves 32 char slots
        .END
