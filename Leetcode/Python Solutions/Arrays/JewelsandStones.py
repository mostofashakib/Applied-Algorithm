"""
LeetCode Problem: 771. Jewels and Stones
Link: https://leetcode.com/problems/jewels-and-stones/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        hashmap = {}
        for i in J:
            if i not in hashmap:
                hashmap[i] = 1
        count = 0
        
        for i in S:
            if i in hashmap:
                count += 1
                
        return count