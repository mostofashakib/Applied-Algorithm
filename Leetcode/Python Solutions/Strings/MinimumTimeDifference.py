"""
LeetCode Problem: 539. Minimum Time Difference
Link: https://leetcode.com/problems/minimum-time-difference/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minTimes = []                                       # An array that sorts the minute representation of an hour
        
        # Traverse through the array
        for time in timePoints:
            hours = int(time[:2])                           # Convert the first segment to hours
            minutes = int(time[3:])                         # Convert the second segment to minutes
            
            minTimes.append(hours*60 + minutes)             # Append the total minutes
            minTimes.append(24*60 + hours*60 + minutes)     # This is done in order to account for anticlockwise difference
            
        minTimes = sorted(minTimes)                         # Sort the min array in an ascending order
        
        minDifference = float('inf')
        
        for index in range(1, len(minTimes)):
            # If two elements in the array have the same value then it is the lowest difference possible hence we just return 0 as our answer
            
            if minTimes[index] == minTimes[index-1]:
                return 0
            minDifference = min(minTimes[index] - minTimes[index-1], minDifference)
            
        return minDifference