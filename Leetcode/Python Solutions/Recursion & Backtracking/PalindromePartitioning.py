"""
LeetCode Problem: 131. Palindrome Partitioning
Link: https://leetcode.com/problems/palindrome-partitioning/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n*2^n)
Space Complexity: O(n)
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1: return [[s]]
        
        def recursiveHelper(index, current):
            if index == len(s):
                result.append(current.copy())                           # Appends a shallow copy of the current partition in the result array
            else:
                for i in range(index+1, len(s)+1):
                    prefix = s[index:i]                                 # Calculates the prefix of a string
                    if prefix == prefix[::-1]:                          # Checks if the prefix is a palindrome or not
                        recursiveHelper(i, current + [prefix])          # If the prefix is a palindrome then recurse
                    
        result = []
        recursiveHelper(0, [])
        return result