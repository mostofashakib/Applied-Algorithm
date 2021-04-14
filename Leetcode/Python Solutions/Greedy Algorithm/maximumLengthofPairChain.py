"""
LeetCode Problem: 646. Maximum Length of Pair Chain
Link: https://leetcode.com/problems/maximum-length-of-pair-chain/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda x:x[1])          # Sort the pairs array by the end time
        count = 1                                           # There is at least one such pair
        previousEndTime = pairs[0][1]                       # Get the initial end time
        length = len(pairs)
        
        for i in range(1, length):
            currentStartTime = pairs[i][0]                  # Get the current start time
            
            # If the previous end time is smaller than the current start time
            # increment the count and update the previous end time
            if previousEndTime < currentStartTime:
                count += 1
                previousEndTime  = pairs[i][1]
        
        return count