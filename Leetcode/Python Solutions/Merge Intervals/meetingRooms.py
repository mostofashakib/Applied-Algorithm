"""
LeetCode Problem: 252. Meeting Rooms
Link: https://leetcode.com/problems/meeting-rooms/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(NlogN)
Space Complexity: O(1)
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key = lambda x: x[1]) # sort based on end time
        length = len(intervals)
        
        for i in range(1, length):
            previousInterval = intervals[i-1]
            currentInterval = intervals[i]
            
            previousEndTime = previousInterval[1]
            currentStartTime = currentInterval[0]
                        
            if previousEndTime > currentStartTime:
                return False 
        
        return True