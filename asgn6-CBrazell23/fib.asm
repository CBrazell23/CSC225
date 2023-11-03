; Recursively computes Fibonacci numbers.
; CSC 225, Assignment 6
; Given code, Winter '20

        .ORIG x4000

; int fib(int)
; TODO: Implement this function.
FIBFN 

        ADD R6, R6, #-1 ; Push space for ret. val.
        ADD R6, R6, #-1 ; Push the return address.
        STR R7, R6, #0
        ADD R6, R6, #-1 ; Push the dynamic link.
        STR R5, R6, #0
        ADD R5, R6, #-1 ; Set the frame pointer.

        ADD R6, R6, #-2
        LDR R0, R5, #4
        LDR R1, R5, #4

        ADD R0, R0, #0
        BRnz NEG
      
        ADD R0, R0, #-1
        BRz BASE
        ADD R0, R0, #1
        
        ADD R6, R6, #-1
        
        ADD R1, R1, #-1
        STR R1, R6, #0
        
        JSR FIBFN
        LDR R2, R6, #0
        ADD R6, R6, #2
        
        STR R2, R5, #0
        LDR R3, R5, #4
        ADD R3, R3, #-2
        
        ADD R6, R6, #-1
        STR R3, R6, #0
        
        JSR FIBFN
        LDR, R4, R6, #0
        ADD R6, R6, #2
        
        STR R4, R5, #-1
        
        LDR R0, R5, #-1
        LDR R1, R5, #0
        ADD R0, R0, R1
        
        STR R0, R5, #3
        BRnzp FIN
      
NEG     AND R3, R3, #0
        STR R3, R5, #3
        BRnzp FIN

BASE    AND R3, R3, #0
        ADD R3, R3, #1
        STR R3, R5, #3
        BRnzp FIN
        
FIN     ADD R6, R6, #2
        LDR R5, R6, #0  ; Pop the dynamic link.
        ADD R6, R6, #1
        LDR R7, R6, #0  ; Pop the return address.
        ADD R6, R6, #1
        RET             ; Return.

      


PROMPT  .STRINGZ "Enter an integer: "
        .END
