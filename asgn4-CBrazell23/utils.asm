; Implements integer I/O utilities.
; CSC 225, Assignment 4
; Given code, Winter '20

        .ORIG x5000     ; NOTE: Do not alter these addresses. They are
        .FILL GETI      ;       hardcoded within "calculator.asm", since the
        .FILL OUTI      ;       assembler cannot resolve cross-file labels.

; Reads one integer in the range {-9, ..., 9}.
;  Takes no arguments.
;  Returns the read integer in R0.
;  TODO: Implement this subroutine.
GETI GETC
   ADD R0, R0, #-15
   ADD R0, R0, #-15
   ADD R0, R0, #-15
   BRz NEG
   
   ADD R0, R0, #-3
   BRnzp FIN
   
NEG GETC
   ADD R0, R0, #-15
   ADD R0, R0, #-15
   ADD R0, R0, #-15
   ADD R0, R0, #-3
   NOT R0, R0
   ADD R0, R0, #1
   
FIN RET

; Prints one integer in the range {-9, ..., 9}.
;  Takes the integer in R0.
;  Returns no values.
;  TODO: Implement this subroutine.
OUTI ST R0, SAVER0
   ST R3, SAVER3
   ADD R0, R0, #0
   BRzp POS
   
   ADD R3, R0, #0
   AND R0, R0, #0
   ADD R0, R0, #15
   ADD R0, R0, #15
   ADD R0, R0, #15
   OUT
   AND R0, R0, #0
   ADD R0, R3, #0
   NOT R0, R0
   ADD R0, R0, #1

POS ADD R0, R0, #15
   ADD R0, R0, #15
   ADD R0, R0, #15
   ADD R0, R0, #3
   OUT
   
   
   LD R0, SAVER0
   LD R3, SAVER3
   RET
SAVER0 .BLKW #2
SAVER3 .BLKW #2
   

        .END
