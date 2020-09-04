"""
LeetCode Problem: 287. Find the Duplicate Number
Link: https://leetcode.com/problems/find-the-duplicate-number/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Solution 1: Floyd's Tortoise and Hare

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]

        # The fast/slow pointers will intersect at some node
        
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
                
        tortoise = nums[0]
        
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        return tortoise

""" Solution 2: Binary Search
There is Binary Search solution with time complexity O(n log n) and space complexity O(1). We have numbers from 1 to n.
Let us choose middle element m = n//2 and count number of elements in list, which are less or equal than m.
If we have m+1 of them it means we need to search for duplicate in [1,m] range, else in [m+1,n] range.
Each time we reduce searching range twice, but each time we go over all data. So overall complexity is O(n log n)
"""

class Solution(object):
    def findDuplicate(self, nums):
        beg, end = 1, len(nums)-1
        
        while beg + 1 <= end:
            mid, count = (beg + end)//2, 0
            for num in nums:
                if num <= mid: count += 1        
            if count <= mid:
                beg = mid + 1
            else:
                end = mid
        return end