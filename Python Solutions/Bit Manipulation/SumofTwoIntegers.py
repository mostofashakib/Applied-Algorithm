"""
LeetCode Problem: 371. Sum of Two Integers
Link: https://leetcode.com/problems/sum-of-two-integers/
Language: Python
Written by: Mostofa Adib Shakib

Algorithm:

Power of two has just one 1-bit.

x & (x - 1) sets this 1-bit to zero, and hence one has to verify if the result is zero x & (x - 1) == 0.

Time complexity :  O(1).
Space complexity : O(1).

Substraction uses the  subtractor logic:

Truth table:

X     Y    Diff     Borrow
0     0     0         0
0     1     1         1
1     0     1         0
1     1     0         0

From the above table, draw the Karnaugh map for “difference” and “borrow”.

Logic equations are:    Diff   = y ^ x
                        Borrow = ~x & y 


Addition uses the adder logic:

Truth table:

X     Y    Diff     Carry
0     0     0         0
0     1     1         0
1     0     1         0
1     1     0         1

From the above table, draw the Karnaugh map for “difference” and “carry”.

Logic equations are:    Diff   = x ^ y
                        Carry =  x & y 
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Case 1 both positive
        
        if a >= 0 and b >= 0:
            return self.addition(a,b)
        
        # Case 2 both negative
        elif a < 0 and b < 0:
            return -self.addition(-a, -b)
        
        # Case 3 a positive and b negative
        elif a >= 0 and b < 0:
            return -self.subtraction(-b,a)
        
        # Case 4 a negative and b positive
        
        elif a < 0 and b >= 0:
            return self.subtraction(a,-b)
        
    def addition(self, x,y):
        while y != 0:
            carry = x & y
            x = x ^ y
            y = carry << 1
        return x
    
    def subtraction(self, x,y):
        while (y != 0):
            borrow = (~x) & y
            x = x ^ y
            y = borrow << 1
        return x