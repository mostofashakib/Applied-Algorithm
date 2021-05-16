"""
LeetCode Problem: 140. Word Break II
Link: https://leetcode.com/problems/word-break-ii/
Reference: https://leetcode.com/problems/concatenated-words/discuss/836924/Python-Template-Word-Break-I-Word-Break-II-Concatenated-Words
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N^2 + 2^N + W)
Space Complexity: O(2^N * N + W)
"""

# Dynamic Programming + Backtracking

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        if not s:
            return [""]
        
        self.res = []
        self.wordDict = set(wordDict)
        self.dp = self.isWordBreak(s, wordDict)
        self.backtrack(s, 0, [])
        
        return self.res
    
    def backtrack(self, s, idx, path):
        # Before we backtrack, we check whether the remaining string 
        # can be splitted by using the dictionary,
        # in this way we can decrease unnecessary computation greatly.
        if self.dp[idx+len(s)]: # if word break possible then only proceed
            if not s:
                self.res.append(' '.join(path))
            else:
                for i in range(1, len(s)+1):
                    if s[:i] in self.wordDict:
                        self.backtrack(s[i:], idx+i, path + [s[:i]])
        
    # this is from Word Break I
    def isWordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp

# Recursion + Memoization

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)

        def topDownRecursive(s):
            """ return list of word lists """
            if not s:
                return [[]]  # list of empty list

            if s in memo:
                # returned the cached solution directly.
                return memo[s]

            for endIndex in range(len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    # move forwards to break the postfix into words
                    for subsentence in topDownRecursive(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            
            return memo[s]

        # break the input string into lists of words list
        topDownRecursive(s)        
        
        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]]