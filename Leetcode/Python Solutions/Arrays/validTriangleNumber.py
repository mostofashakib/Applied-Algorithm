"""
LeetCode Problem 611. Valid Triangle Number
Link: https://leetcode.com/problems/valid-triangle-number/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Binary Search
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0
        
        nums.sort()
        ans = 0
        
        for i in range(2, len(nums)):
            left = 0
            right = i - 1
            
            while left < right:
                if nums[left] + nums[right] <= nums[i]:
                    left += 1
                else:
                    # here, we know that nums[left] + nums[right] > nums[i]
                    # automatically, nums[left + 1] + nums[right] > nums[i]
                    # and so on
                    ans += right - left
                    right -= 1
        
        return ans

# Nested Loop
# Time Complexity: O(N^2)
# Space Complexity: O(1)


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        count = 0
        i = 0
        
        while i < length-2:
            k = i + 1
            
            while k < length-1:
                j = k + 1            
                while j < length:
                    if nums[i] + nums[k] > nums[j]:
                        count += 1
                    else:
                        break
                    j += 1
                k += 1
            i += 1
        
        return count