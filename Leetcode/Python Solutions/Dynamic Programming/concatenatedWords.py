"""
LeetCode Problem: 472. Concatenated Words
Link: https://leetcode.com/problems/concatenated-words/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N^4)
Space Complexity: O(N)
"""

class Solution:
    def workBreak(self, word, wordDict):
        if not word:
            return False
        
        n = len(word)
        dp = [False for i in range(n+1)]
        dp[0] = True
        
        for i in range(n+1):
            for j in range(i):
                if dp[j] and word[j:i] in wordDict:
                    dp[i] = True
                    break
                    
        return dp[-1]
        
        
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if not words:
            return []
        
        result = []
        words.sort(key = len)
        wordDict = set()
        
        
        for word in words:
            if self.workBreak(word, wordDict):
                result.append(word)
            wordDict.add(word)
        
        return result