"""
LeetCode Problem: 91. Decode Ways
Link: https://leetcode.com/problems/decode-ways/
Reading Material: https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-%2B-DFS)
Language: Python
Written by: Mostofa Adib Shakib
"""

# Dynamic Programming
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        
        for i in range(2, n+1):
            oneDigit = s[i-1:i]
            twoDigit = s[i-2:i]
            
            if oneDigit != "0":
                dp[i] += dp[i-1]
                
            if twoDigit[0] != "0" and 10 <= int(twoDigit) <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]


# Recursion + Memoization
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def numDecodings(self, s:str) -> int:
        if len(s) == 0 or s is None:
            return 0

        @lru_cache(maxsize=None)
        def dfs(string):
            if len(string)>0:
                if string[0] == '0':
                    return 0
            if string == "" or len(string) == 1:
                return 1
            if int(string[0:2]) <= 26:
                first = dfs(string[1:])
                second = dfs(string[2:])
                return first+second
            else:
                return dfs(string[1:])

        return dfs(s)