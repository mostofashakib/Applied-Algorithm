"""
LeetCode Problem: 1119. Remove Vowels from a String
Link: https://leetcode.com/problems/remove-vowels-from-a-string/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeVowels(self, S: str) -> str:
        string = ""
        hashmap = {'a': 1, 'e':1, 'i':1, 'o':1, 'u':1}  # A hashmap that contains all the vowels
        
        for i in S:                                     # Traverse the input string S character by character
            if i not in hashmap:                        # Check to see if the character is a vowel or not
                string += i                             # If the character is not a vowel concatenate the character with the string.
        return string