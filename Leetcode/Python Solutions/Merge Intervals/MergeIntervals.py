"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
"""

"""

Edge case:
1) If the length of the interval list is 0. return []
2) If the length of the interval list is 1 return intervals as the intervals list only has one
interval.

Conditions to check:
1) If the maximum value of the previous interval is greater than or equal to the minimum value
of the current interval if so then we have an overlap.
2) If the maximum value of the previous interval is greater than the minimum value of the 
current interval then there is no overlap and we append the interval to the result.

This solution uses two pointers. One global pointer which initially points to the first interval
in a list of intervals. The second pointer starts from the second interval in the list of
intervals and check to see if the maximum element of the global pointer is greater than or equal
to the minimum value of the local pointer in order to check if both  the intervals overlaps.
If they overlap then we change the value for the maximum value of the global pointer but
inputing the highest value between the current global maximum and the local maximum and we
continue to do this up until the first codition holds if not then we append the result to a list
and reset the global pointer to the interval next to the interval we just appended to the result
list. At the end of the iteration we append the last interval to the resulting list but 
appending the value of the globalmin and globalmax.

"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
                
        if len(intervals) <= 1: return intervals
        
        Sintervals = sorted(intervals)
                
        GlobalMin = Sintervals[0][0]
        GlobalMax = Sintervals[0][1]

        merged = []
        
        for i in range(1, len(Sintervals)):
            LocalMin = Sintervals[i][0]
            LocalMax = Sintervals[i][1]

            if LocalMin <= GlobalMax:  # overlapping intervals
                GlobalMax = max(LocalMax, GlobalMax)
            else:  # non-overlapping interval, add the previous interval and reset
                merged.append([GlobalMin, GlobalMax])
                GlobalMin = LocalMin
                GlobalMax = LocalMax
            
        merged.append([GlobalMin, GlobalMax])  # add the last interval

        return merged