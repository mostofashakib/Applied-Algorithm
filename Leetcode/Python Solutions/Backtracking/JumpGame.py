"""
LeetCode Problem: 55. Jump Game
Link: https://leetcode.com/problems/jump-game/
Language: Python
Written by: Mostofa Adib Shakib

"""

# Brute-Force solution
# Time Complexity: O(2!)
# Space Complexity: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        
        startingIndex = 0
        endingIndex = len(nums) -1
        
        def helper(idx, target, currVal):
            if idx == target: return True
            if currVal == 1:
                if helper(idx+1, target, nums[idx+1]) == True:
                    return True
            if idx < target and currVal != 0:
                for i in range(1,currVal+1):
                    if i+idx <= target:
                        if helper(idx+i, target, nums[idx+i]) == True:
                            return True
                    
            return False
                    
        return helper(startingIndex, endingIndex, nums[startingIndex])


# Backtracking
# Time Complexity: O(2^n)
# Space Complexity: O(n)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        def backtrack(index, arr):
            n = len(arr) -1
            if index == n: return True     # base base
            
            furthestStep = min(index+arr[index], n)  #further step you can jump from a given position
            
            for i in range(furthestStep, index, -1): # checks to see if you can reach the end from a given position
                if backtrack(i, arr) == True:
                    return True
                
            return False
        
        if not nums: return
        
        return backtrack(0, nums)


# Greedy algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        index = len(nums) - 1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= index:
                index = i
                
        return index == 0