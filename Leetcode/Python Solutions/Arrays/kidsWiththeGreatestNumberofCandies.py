"""
LeetCode Problem: 1431. Kids With the Greatest Number of Candies
Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        length = len(candies)
        result = [False for i in range(length)]
        
        for i in range(length):
            if candies[i] + extraCandies >= maximum:
                result[i] = True
                
        return result