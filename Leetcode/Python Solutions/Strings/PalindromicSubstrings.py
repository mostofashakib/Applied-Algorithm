"""
LeetCode Problem: 647. Palindromic Substrings
Link: https://leetcode.com/problems/palindromic-substrings/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Expand from the center
# Time complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        # So we know palindromes can be centered around, s[i] or around s[i],s[i+1]
        length, ans = len(s), 0

        # Cound odd palindromes
        for i in range(length):
            l, r = i, i
            while l >= 0 and r <= length-1 and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1

        # Count even palindromes
        for j in range(length-1):
            l, r = j, j+1
            while l >= 0 and r <= length-1 and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1

        return ans


# Brute Force
# Time complexity: O(n^3)
# Space Complexity: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # This function checks if a particular string is a palindrome or not
        def isPalindrome(string):
            return string == string[::-1]
        
        ans = 0
        
        for i in s:
            ans += 1
        
        for i in range(len(s)):
            for j in range(i):
                substring = s[j:i+1]
                if isPalindrome(substring) and len(substring) > 1:
                    ans += 1
                        
        return ans
        