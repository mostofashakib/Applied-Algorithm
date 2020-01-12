"""
LeetCode Problem: 759. Employee Free Time
Link: https://leetcode.com/problems/employee-free-time/
Language: Python
Written by: Mostofa Adib Shakib

Algorithm:
1) Add all the intervals into a list
2) Merge overlapping intervals
3) Find the gap in the merged intervals

Time Complexity:  N*log(N)
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if len(schedule) < 2:
            return []

        intervals = []                         # keeps the times in an array
        for employee in schedule:
            for interval in employee:
                intervals.append(interval)
        
        res = []                                  # result array
        intervals.sort(key = lambda x: x.start)   #  sort by start time
        
        cur_start = intervals[0].start            # global startTime
        cur_end   = intervals[0].end              # global endTime
        
        for i in intervals[1:]:            
            if i.start > cur_end:                   # finding the gap between merged intervals
                res.append(Interval(cur_end, i.start))         
            
            cur_end  = max(cur_end, i.end)  # overlapping intervals so merge them
                     
        return res    # return the result

