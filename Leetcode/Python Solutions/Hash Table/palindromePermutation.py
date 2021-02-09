"""
LeetCode Problem: 266. Palindrome Permutation
Link: https://leetcode.com/problems/palindrome-permutation/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashmap = {}
        
        # Getting the frequency of each character in the string
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
                
        counter = 0

        for key, value in hashmap.items():
            # Count the number of characters with odd frequencies
            if value % 2 == 1:
                counter += 1
                
                # If more than one character has odd frequencies then a palindrome cannot be formed
                if counter > 1:
                    return False

        return True