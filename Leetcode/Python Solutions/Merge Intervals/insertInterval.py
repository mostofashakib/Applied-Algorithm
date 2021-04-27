"""
LeetCode Problem: 57. Insert Interval
Link: https://leetcode.com/problems/insert-interval/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        result = []
        intervalStartTime = newInterval[0]
        intervalEndTime = newInterval[1]
        idx = 0
        length = len(intervals)
        
        while idx < length and intervals[idx][1] < intervalStartTime:
            result.append(intervals[idx])
            idx += 1
            
        if idx == length:
            result.append(newInterval)
            return result
        
        if intervalEndTime < intervals[idx][0]:
            intervals.insert(idx, newInterval)
            return intervals
        
        localMinimum = min(intervals[idx][0], intervalStartTime)
        localMaximum = max(intervals[idx][1], intervalEndTime)
        
        idx += 1
        
        while idx < length:
            startTime = intervals[idx][0]
            endTime = intervals[idx][1]
            
            if startTime <= localMaximum:
                localMinimum = min(startTime, localMinimum)
                localMaximum = max(localMaximum, endTime)
            else:
                result.append([localMinimum, localMaximum])
                localMinimum = startTime
                localMaximum = endTime
            
            idx += 1
        
        result.append([localMinimum, localMaximum])
        return result