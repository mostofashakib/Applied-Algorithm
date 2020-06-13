"""
LeetCode Problem: 75. Sort Colors
Link: https://leetcode.com/problems/sort-colors/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity : O(N)
Space complexity : O(1)

Algorithm:

Initialise the rightmost boundary of zeros : p0 = 0. During the algorithm execution nums[idx < p0] = 0.

Initialise the leftmost boundary of twos : p2 = n - 1. During the algorithm execution nums[idx > p2] = 2.

Initialise the index of current element to consider : curr = 0.

While curr <= p2 :

    If nums[curr] = 0 : swap currth and p0th elements and move both pointers to the right.

    If nums[curr] = 2 : swap currth and p2th elements. Move pointer p2 to the left.

    If nums[curr] = 1 : move pointer curr to the right.

"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration
        p1 = 0
        
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1
        iterator = 0
        
        while iterator <= p2:
            if nums[iterator] == 0:
                nums[iterator], nums[p1] = nums[p1], nums[iterator]
                p1 += 1
                iterator += 1
            elif nums[iterator] == 2:
                nums[iterator], nums[p2] = nums[p2], nums[iterator]
                p2 -= 1
            else:
                iterator += 1