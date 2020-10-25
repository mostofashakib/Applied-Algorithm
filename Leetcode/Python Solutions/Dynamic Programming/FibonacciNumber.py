"""
LeetCode Problem: 509. Fibonacci number
Link: https://leetcode.com/problems/fibonacci-number/
Language: Python
Written by: Mostofa Adib Shakib

"""

class Solution(object):
    def fib(self, n):
        
        f = [0, 1]
        for i in range(2, n+1):
            f.append(f[i-1]+f[i-2])
        return f[n]
             