"""

LeetCode Problem: . Two Sum
Link: https://leetcode.com/problems/two-sum/
Written by: Mostofa Adib Shakib
Language: Python

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        low = 0
        high = len(nums) - 1
        ans = []
        result = []
        numSA = sorted(nums)
        
        while low < high:
            if numSA[low] + numSA[high] < target:
                low += 1
            elif numSA[low] + numSA[high] > target:
                high -= 1 
            elif numSA[low] + numSA[high] == target:
                ans.append([numSA[low], numSA[high]])
                low += 1
                high -= 1
        
        
        for i in range(len(nums)):
            if nums[i] in ans[0]:
                result.append(i)
        return result