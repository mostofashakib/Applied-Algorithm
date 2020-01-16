"""

LeetCode Problem: 279. Perfect Squares
Link: https://leetcode.com/problems/perfect-squares/
Language: Python
Written by: Mostofa Adib Shakib

A = Amount till which perfect squares can exist
C = Total number of perfect squares

Time complexity: O(A * C)
Space complexity: O(A)

"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [ float('inf') for i in range(n+1) ]      # A lookup array
        rng = int( n**(0.5) )                          # the maximum number till which we can find the perfect squares
        dp[0] = 0                                      # if the amount is zero then the number of perfect squares will always be 0

        squares = [i**2 for i in range(1, rng+1)]      # An array containing all the possible perfect squares
                
        for sqr in squares:                            # checks each squares again the amount to calculate the minimum perfect squares
            for i in range(sqr, n+1):                  
                dp[i] = min(dp[i], dp[i-sqr] + 1)      # finds the minimum between the previously computed minimum and the current state.
                
        return dp[-1] if dp[-1] != float('inf') else 0     # returns the minimum number of perfect squares if it exists
