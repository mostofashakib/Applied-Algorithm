"""
LeetCode Problem: 139. Word Break
Link: https://leetcode.com/problems/word-break/
Video Explanation: https://www.youtube.com/watch?v=tSbBuiO1rXI
Written by: Mostofa Adib Shakib
Language: Python
"""

""" Recursion + Memoization
Let dfs(k) be a possibility to split string s[k:] into words from wordSet. Then to check if word s[k:] can be splitted,
we need to check if for some i word s[k:i] in our wordSet and if s[i:] can be splitted, which is dfs(i).

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        
        @lru_cache(maxsize=None)
        def dfs(index):
            if index == len(s):
                return True
            
            for i in range(index+1, len(s)+1):
                if s[index:i] in wordDict and dfs(i):
                    return True
                
            return False
        
        return dfs(0)


# Dynamic Programming
# Time Complexity: O(n*m)
# Space Complexity: O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        dp = [True] + [False] * n
        
        for i in range(1, n+1):
            for word in wordDict:
                if dp[i-len(word)] and s[:i].endswith(word):
                    dp[i] = True
                    
        return dp[-1]