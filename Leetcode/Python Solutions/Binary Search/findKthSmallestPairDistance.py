"""
LeetCode Problem 719. Find K-th Smallest Pair Distance
Link: https://leetcode.com/problems/find-k-th-smallest-pair-distance/
Written by: Mostofa Adib Shakib
Language: Python

Time complexity: O(nlogn)
Space complexity: O(1)
"""

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0                         # Lowest possible distance
        high = nums[-1] - nums[0]       # Highest possible distance
        
        # binary search
        while low <= high:
            windowSize = 0              # Sliding window size
            right = 0                   # Right most pointer
            mid = (low+high)//2         # possible min distance
            length = len(nums)          # length of the array
            
            # Traverse the left pointer
            for left in range(length):
                # find the right most position up until we can find pairs
                while j < length and nums[right] - nums[left] <= mid:
                    right += 1
                
                # Calculate the window size
                windowSize += (right-left-1)
            
            # If the window size is bigger or equal than k then we overshoot our estimation
            if windowSize >= k:
                high = mid - 1
                
            # If the window size is smaller than k then we undershoot our estimation
            else:
                low = mid + 1
                    
        return low      # return the minimum absolute distance