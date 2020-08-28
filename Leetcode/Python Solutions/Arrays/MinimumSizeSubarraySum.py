"""
LeetCode Problem: 209. Minimum Size Subarray Sum
Link: https://leetcode.com/problems/minimum-size-subarray-sum/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Solution 1
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        
        runningSum = 0
        
        runningTotal = [nums[0]]
        runningSum += nums[0]
        startingPoint = 1
        length = float('inf')
        
        while len(runningTotal):
            if runningSum < s and startingPoint < len(nums):
                runningTotal.append(nums[startingPoint])
                runningSum += nums[startingPoint]
                startingPoint += 1
            elif runningSum >= s:
                length = min(length, len(runningTotal))
                value = runningTotal.pop(0)
                runningSum -= value
                if runningSum >= s:
                    length = min(length, len(runningTotal))
            else:
                break
                    
        return length if length != float('inf') else 0

# Solution 2
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        
        left = 0
        min_len = float('inf')
        
        nums_sum = 0
        
        for right in range(len(nums)):
            nums_sum += nums[right]
            while nums_sum >= s:
                min_len = min(min_len, right-left+1)
                nums_sum -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0