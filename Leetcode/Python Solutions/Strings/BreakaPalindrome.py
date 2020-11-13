"""
LeetCode Problem 1328. Break a Palindrome

Link: https://leetcode.com/problems/break-a-palindrome/
Written by: Mostofa Adib Shakib
Language: Python
"""

# Optimal Solution
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # Palindrome is of length 1, so there's no way to break it 
        if len(palindrome) == 1:
            return ""
        
        # Get index of first non "a" char
        idx = -1
        
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                idx = i
                break
                
        # Case 1: palindrome is all a's, so just replace last "a" with "b"
        if idx == -1:
            return palindrome[:-1] + "b"
        
        # Case 2: Replace the first non "a" char with "a"
        return palindrome[:idx] + "a" + palindrome[idx + 1:]


# Brute Force Solution
# Time Complexity: O(n^2)
# Space Complexity: O(n)


from string import ascii_lowercase

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        # A helper function that returns True if an input string is not a palindrome.
        def isPalindrome(string):
            return string != string[::-1]
        
        # If the length of the string is 1 then return the empty string
        if len(palindrome) == 1:
            return ""

        originalPalindrome = palindrome     # Keeps a copy of the original Palindrome
        palindrome = list(palindrome)       # Change the palindrome's data structure from a string to a list of characters
        possiblePalindromes = []            # Stores all the possible Palindromes
        
        # For every character in a palindrome change it to every single lowercased alphabet then append the string if it is not a palindrome
        for i in range(len(palindrome)):
            for char in ascii_lowercase:
                temp = palindrome[i]        # Keeps a copy of the original character
                palindrome[i] = char
                
                tempPalindrome = ''.join(palindrome)
                                
                if isPalindrome(tempPalindrome):
                    possiblePalindromes.append(tempPalindrome)
                
                palindrome[i] = temp        # After all possible alphabets have been match replace it back with the original character
        
        # If the length of the possiblePalindromes is greater than one than sorted it lexicographically and return the first element
        if possiblePalindromes:
            return sorted(possiblePalindromes)[0]
        
        # If the length of the possiblePalindromes is less than one than return an empty string
        return ""