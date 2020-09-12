"""
LeetCode Problem: 132. Palindrome Partitioning II
Link: https://leetcode.com/problems/palindrome-partitioning-ii/
Language: Python
Written by: Mostofa Adib Shakib

"""

# Optimized Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def minCut(self, s: str) -> int:
        # If the given string is already a palindrome
        if s == s[::-1]: return 0

        # Optimization
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
            
        n = len(s)
        
        cut = [0 for i in range(n)]
        isPalindrome = [ [False for i in range(n)] for j in range(n) ]
        
        for i in range(1, n):
            minimum = i             # Set maximum # of cut
            
            for j in range(0, i+1):
                # If palindrome no need to cut else add 1 to the previous cut[i-1]
                if s[i] == s[j] and (i <= j + 1 or isPalindrome[i - 1][j + 1]):
                    isPalindrome[i][j] = True
                    minimum = min(minimum, 0 if j == 0 else 1 + cut[j - 1])
            cut[i] = minimum
                
        return cut[-1]

# Naive Recusion + Memoization
# Time Complexity: O(n^3)
# Space Complexity: O(n)

class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrome(x): 
            return x == x[::-1] 
        
        @lru_cache(maxsize=None)
        def minPalPartion(string, i, j):
            if i >= j or isPalindrome(string[i:j + 1]): 
                return 0
            ans = float('inf') 
            for k in range(i, j): 
                count = (1 + minPalPartion(string, i, k) + minPalPartion(string, k + 1, j) )
                ans = min(ans, count) 
            return ans
        
        return minPalPartion(s, 0, len(s) - 1)

# Dynamic Programming
# Time Complexity: O(n^3)
# Space Complexity: O(n^2)

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        isPalindrome = [ [ False for i in range (n) ] for i in range(n) ]
        minimumCuts = [ [ 0 for i in range (n) ] for i in range(n) ]
        
        for i in range(n):
            isPalindrome[i][i] = True
            minimumCuts[i][i] = 0
            
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                
                if length == 2:  
                    isPalindrome[i][j] = (s[i] == s[j]) 
                else: 
                    isPalindrome[i][j] = ((s[i] == s[j]) and isPalindrome[i + 1][j - 1]) 
                
                if isPalindrome[i][j]:
                    minimumCuts[i][j] = 0
                
                else:
                    minimumCuts[i][j] = float('inf')
                    for k in range(i, j):
                        minimumCuts[i][j] = min(minimumCuts[i][j], minimumCuts[i][k] + minimumCuts[k+1][j] + 1)
                        
        return minimumCuts[0][-1]