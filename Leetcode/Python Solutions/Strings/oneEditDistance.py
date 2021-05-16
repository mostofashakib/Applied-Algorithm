"""
LeetCode Problem: 161. One Edit Distance
Link: https://leetcode.com/problems/one-edit-distance/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isOneEditDistance(self, word1: str, word2: str) -> bool:
        n = len(word1)
        m = len(word2)
        
        if n > m:
            return self.isOneEditDistance(word2, word1)
        
        if abs(m - n) > 1 or m == n and word1 == word2:
            return False
        
        
        edited = False
        p1 = 0
        p2 = 0
        
        while p1 < n and p2 < m:
            if word1[p1] == word2[p2]:
                p1 += 1
            else:
                if edited:
                    return False
                
                edited = True
                
                if n == m:
                    p1 += 1
                
            p2 += 1
            
        return True