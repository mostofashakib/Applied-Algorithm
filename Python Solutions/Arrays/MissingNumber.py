"""
LeetCode Problem: 268. Missing Number
Link: https://leetcode.com/problems/missing-number/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""
Approach 1:
Sum of numbers from 1 to n: n(n+1)//2
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumShouldBe = (len(nums) + 1) * len(nums) // 2
        actualSum = sum(nums)
        return sumShouldBe - actualSum


"""
Approach 2:
Time Complexity: O(logn)
Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i == nums[i]:
                continue
            elif i < len(nums):
                return i
            
        return len(nums)