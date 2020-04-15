"""
LeetCode Problem: 387. First Unique Character in a String.
Link: https://leetcode.com/problems/first-unique-character-in-a-string/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        
        hashmap = {}
        
        for index in range(len(s)):
            if s[index] not in hashmap:
                hashmap[s[index]] = [1, index]
            else:
                hashmap[s[index]] = [float('-inf'), index]
                
        for key, value in hashmap.items():
            if value[0] == 1:
                return value[1]
        
        return -1
