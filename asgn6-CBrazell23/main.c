#include <stdio.h>
#include "fib.h"

/*
 * Recursively computes Fibonacci numbers.
 * CSC 225, Assignment 6
 * Given code, Winter '20
 * TODO: Complete this file.
 */

int fib(int x){
   if(x <= 0){
      return 0;
   }
   if(x == 1){
      return x;
   }
   return fib(x - 1) + fib(x - 2);
}

int main(void) {
   int x;
   printf("Enter an integer: ");
   scanf("%d", &x);
   printf("f(%d) = %d\n", x, fib(x));
   return 0;
}
