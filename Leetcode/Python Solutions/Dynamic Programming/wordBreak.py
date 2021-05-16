"""
LeetCode Problem: 139. Word Break
Link: https://leetcode.com/problems/word-break/
Video Explanation: https://www.youtube.com/watch?v=tSbBuiO1rXI
Written by: Mostofa Adib Shakib
Language: Python
"""

# Dynamic Programming
# Time Complexity: O(n^3)
# Space Complexity: O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        dp = [True] + [False] * n
        
        for i in range(1, n+1):
            for word in wordDict:
                if dp[i-len(word)] and s[:i].endswith(word):
                    dp[i] = True
                    break
                    
        return dp[-1]


""" Recursion + Memoization
Let recursiveHelper(k) be a possibility to split string s[k:] into words from wordSet. Then to check if word s[k:] can be splitted,
we need to check if for some i word s[k:i] in our wordSet and if s[i:] can be splitted, which is recursiveHelper(i).

Time Complexity: O(n^3)
Space Complexity: O(n)
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        
        @lru_cache(maxsize=None)
        def recursiveHelper(index):
            if index == len(s):
                return True
            
            for i in range(index+1, len(s)+1):
                if s[index:i] in wordSet and recursiveHelper(i):
                    return True
                
            return False
        
        return recursiveHelper(0)