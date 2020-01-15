"""
LeetCode Problem 167. Two Sum II - Input array is sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Written by: Mostofa Adib Shakib
Language: Python
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: return []
        
        FirstPointer = 0
        LastPointer = len(numbers) - 1
        result = []

        while FirstPointer < LastPointer:
            if numbers[FirstPointer] + numbers[LastPointer] == target:
                result.append(FirstPointer+1)
                result.append(LastPointer+1)
                break
            elif numbers[FirstPointer] + numbers[LastPointer] > target:
                LastPointer -= 1
            else:
                FirstPointer += 1
        return result
        