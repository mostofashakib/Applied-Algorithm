"""
LeetCode Problem: 775. Global and Local Inversions
Link: https://leetcode.com/problems/global-and-local-inversions/
Language: Python
Written by: Mostofa Adib Shakib

Key observations: 

1) Return True the number of global inversions needs to be equal to the number of local inversions.
2) All local inversions are also global inversions.
3) Return False as soon as we encounter a global inversion which is not a local inversion.
"""

# Optimal Solution
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        length = len(A)
        maximum = -1
        
        for i in range(length-2):
            maximum = max(maximum, A[i])
            
            if maximum > A[i+2]:
                return False
            
        return True

# Brute Force + Enhanced Merge Sort
# Time Complexity: O(NLogN)
# Space Complexity: O(N)

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        globalInversions = 0
        localInversions = 0
        length = len(A)
        
        for i in range(1, length):
            if A[i-1] > A[i]:
                localInversions += 1
        
        def divideNConquer(nums):
            
            if len(nums) < 2:
                return 0
            
            mid = len(nums)//2
            
            count = 0
            
            count += divideNConquer(nums[:mid])
            count += divideNConquer(nums[mid:])
            
            nums = sorted(nums[:mid]) + sorted(nums[mid:])
            
            le = 0
            ri = mid
            
            while le < mid and ri < len(nums):
                while le < mid and nums[le] <= nums[ri]:
                    le += 1
                count += mid - le
                ri += 1
            
            return count
        
        globalInversions = divideNConquer(A)
        
        if globalInversions == localInversions:
            return True
        else:
            return False