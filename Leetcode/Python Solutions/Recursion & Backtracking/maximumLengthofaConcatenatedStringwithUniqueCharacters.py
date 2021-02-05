"""
LeetCode Problem: 1239. Maximum Length of a Concatenated String with Unique Characters
Link: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def isUnique(string):
            if len(string) == len(set(string)):
                return True
            else:
                return False

        def helper(arr, comb, start):
            if isUnique(comb):
                self.ans = max(self.ans, len(comb))
            else:  # has duplicates
                return

            for i in range(start, len(arr)):
                helper(arr, comb + arr[i], i + 1)
                
        self.ans = 0
        helper(arr, '', 0)
        return self.ans