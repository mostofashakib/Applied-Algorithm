"""
LeetCode Problem 1413. Minimum Value to Get Positive Step by Step Sum
Link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
Language: Python
Written by: Mostofa Adib Shakib
"""

""" Faster
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        runningSum = 0
        minimumSoFar = 0
        for i in nums:
            runningSum = runningSum + i
            minimumSoFar = min(minimumSoFar, runningSum)
        return max(1, 1-minimumSoFar)
   
""" Brute Force - very slow
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = float('inf')

        for i in range(1,2000):
            startValue = i
            count = 0
            for j in range(len(nums)):
                if j == 0:
                    count = startValue + nums[j]
                    if count  < 1:
                        break
                else:
                    count += nums[j]
                    if count  < 1:
                        break

            if count >= 1:
                ans = min(ans, startValue)
        return ans
        
    