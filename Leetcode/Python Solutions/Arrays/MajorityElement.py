"""
LeetCode 169. Majority Element
Link: https://leetcode.com/problems/majority-element/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: (n)
Space Complexity: O(n)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        maximum = [0,0]
        
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        for key, value in hashmap.items():
            if value > maximum[1]:
                maximum = [key, value]
                
        return maximum[0]
