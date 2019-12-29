"""
LeetCode Problem: 1095. Find in Mountain Array
Link: https://leetcode.com/problems/find-in-mountain-array/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        #binary search to find the peak mountain
        
        high = mountain_arr.length() -1
        low = 0
        
        while(low<high):
            mid = (low+high)//2
            if mountain_arr.get(mid) > mountain_arr.get(mid+1):
                high = mid
            else:
                low = mid+1
        peak = low
        
        #binary search to find target in the acsending part of the array

        low = 0
        high = peak+1
        while(low<high):
            mid = (low+high)//2
            temp = mountain_arr.get(mid)
            if target==temp: return mid
            if temp>target:
                high = mid
            else:
                low = mid+1

        #binary search to find target in the descending part of the array

        low = peak+1
        high = mountain_arr.length()
        while(low<high):
            mid = (low+high)//2
            temp = mountain_arr.get(mid)
            if target==temp: return mid
            if temp<target:
                high = mid
            else:
                low = mid+1  

        return -1   # returns -1 if target not found in the mountain array