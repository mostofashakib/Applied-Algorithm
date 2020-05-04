"""
LeetCode Problem 1009. Complement of Base 10 Integer
Link: https://leetcode.com/problems/complement-of-base-10-integer/
Written by: Mostofa Adib Shakib
Language: Python
"""

# Solution 1: Bit Manipulation
# Time complexity: O(1)  Since the number of iterations is not more than 32.
# Space complexity: O(1)

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        
        mask = 1
        amount = N
        
        while amount:
            N = N ^ mask
            mask = mask << 1
            amount = amount >> 1
            
        return N


# Solution 2: String Manipulation 
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findComplement(self, num: int) -> int:
        nums = bin(num)
        string = ''
        
        for i in str(nums)[2:]:
            if i == '0':
                string += '1'
            else:
                string += '0'
                
        return int(string, 2)   # converts string to an interger in base 2 form