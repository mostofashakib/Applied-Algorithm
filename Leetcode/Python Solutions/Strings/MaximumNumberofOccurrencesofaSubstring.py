"""
LeetCode Problem: 1297. Maximum Number of Occurrences of a Substring
Link: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        maps = {}
        n = len(s)
        res = 0
        
        for i in range(n-minSize+1):
            sub = s[i:i+minSize]
            if len(set(sub)) < =maxLetters:
                # if the key does not exist then it returns 0
                maps[sub] = maps.get(sub,0) + 1
                res = max(res, maps[sub])
        return res