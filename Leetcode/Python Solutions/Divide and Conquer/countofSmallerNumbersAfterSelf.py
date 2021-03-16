"""
LeetCode Problem: 315. Count of Smaller Numbers After Self
Link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

class Solution:
    def countSmaller(self, nums):
        tmp = [0] * len(nums)
        res = [0] * len(nums)
        nums = list(enumerate(nums))
        self.mergeSort(nums, 0, len(nums) - 1, tmp, res)
        return res
    
    def mergeSort(self, nums, start, end, tmp, res):
        if start >= end:
            return
        
        mid = start + (end - start) // 2
        
        self.mergeSort(nums, start, mid, tmp, res)
        self.mergeSort(nums, mid + 1, end, tmp, res)
        i, j, k = start, mid + 1, start
        cnt = 0
        
        while i <= mid and j <= end:
            if nums[i][1] <= nums[j][1]:
                tmp[k] = nums[i]
                res[nums[i][0]] += cnt
                i += 1
            else:
                tmp[k] = nums[j]
                cnt += 1
                j += 1
            k += 1
            
        while i <= mid:
            tmp[k] = nums[i]
            res[nums[i][0]] += cnt
            i += 1
            k += 1
            
        while j <= end:
            tmp[k] = nums[j]
            j += 1
            k += 1
        for k in range(start, end + 1):
            nums[k] = tmp[k]
        return