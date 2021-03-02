"""
LeetCode Problem 1151. Minimum Swaps to Group All 1's Together
Link: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        countOnes = sum(data)
        length = len(data)
        runningCount = data[0]
        right = 1
        left = 0
        maximumOnes = 0
        
        while right < length:
            runningCount += data[right]
            
            if right - left == countOnes:
                runningCount -= data[left]
                left += 1
                
            maximumOnes = max(maximumOnes, runningCount)
            right += 1
        
        return countOnes - maximumOnes