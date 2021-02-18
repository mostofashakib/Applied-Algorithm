"""

LeetCode Problem: 214. Shortest Palindrome
Link: https://leetcode.com/problems/shortest-palindrome/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n^2)
Space Complexity: O(n)

"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:

        # Helper function to check if a given string is a palindrome
        def isPalindrome(string):
            return string == string[::-1]
        
        # edge case
        if len(s) <= 1 or isPalindrome(s):
            return s

        i = len(s) - 1
        output = ""
        
        while i >= 0:
            output += s[i]
            # Check after adding each character to the output string
            if isPalindrome(output + s):
                return output + s
            i -= 1
            
        return output + s