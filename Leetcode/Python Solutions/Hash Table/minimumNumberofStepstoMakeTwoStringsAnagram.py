"""
LeetCode Problem: 1347. Minimum Number of Steps to Make Two Strings Anagram
Link: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashMap = {}
        count = 0

        for char in s:
            if char not in hashMap:
                hashMap[char] = 1
            else:
                hashMap[char] += 1
        
        for char in t:
            if char in hashMap and hashMap[char] > 0:
                hashMap[char] -= 1
            else:
                count += 1
        
        return count