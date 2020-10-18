"""
LeetCode Problem 29. Divide Two Integers

Link: https://leetcode.com/problems/divide-two-integers/
Written by: Mostofa Adib Shakib
Language: Python

Time complexity: O(log n)
Space complexity: O(1)
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        # Special case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # convert everything to negative since the negative range is bigger
        # Keep track of how many negative signs we have seen so far
        
        numOfNegatives = 2
        
        if dividend > 0:
            dividend = -dividend
            numOfNegatives -= 1
        if divisor > 0:
            divisor = -divisor
            numOfNegatives -= 1
        
        # This keeps track of the number of copies of the divisor that makes up the largest double
        
        powerOfTwos = 1
        maximumDouble = divisor
        
        # calculate the maximum value than can be taken out from the dividend
        
        while dividend <= maximumDouble+maximumDouble:
            powerOfTwos += powerOfTwos
            maximumDouble += maximumDouble
            
        quotient = 0
        
        # we keep adding to the quotient up until the divided is smaller than the divisor
        
        while dividend <= divisor:
            # This checks that the current maximumDouble can fit in the dividend 
            if dividend <= maximumDouble:
                dividend -= maximumDouble
                quotient += powerOfTwos
                
            # Do a bitwise left shift to divide the number by 2
            maximumDouble = maximumDouble >> 1
            powerOfTwos = powerOfTwos >> 1
        
        # Answer is negative only if one of the signs are negative else it is positive
        
        return quotient if numOfNegatives != 1 else -quotient