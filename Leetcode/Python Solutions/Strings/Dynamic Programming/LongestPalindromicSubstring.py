"""
LeetCode Problem: 5. Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/
Written by: Mostofa Adib Shakib
Language: Python

"""

"""

A palindrome can only be of two forms

Even length: two center elements
Odd length: one center element

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or s == s[::-1]: return s # checks if it's an empty string or if the given string is a palindrome
        
        res = ""
    
        for i in range(len(s)):
            temp = self.palindrome(s, i, i) # incase of odd length
            
            if len(temp) > len(res):  res = temp
                
            temp = self.palindrome(s, i ,i+1) #incase of even length
            
            if len(temp) > len(res):  res = temp
        
        return res  #returns the answer
                
    def palindrome(self, s, left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]: #checks if the string is palindrome
            left  -= 1    # decrement the index of left by 1
            right += 1    # increment the index of right by 1

        return s[left+1: right]   #returns  the longest palindromic substring of a given string
    


