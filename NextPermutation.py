"""
LeetCode Problem: 31. Next Permutation
Link: https://leetcode.com/problems/next-permutation/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)

Algorithm:

1) Find k such that array[k] < array[k+1]. This is the decreasing part called the suffix
2) initialize e = array[k]  the element just before the suffix
    if e doesn't exist then return the reverse of the initial array
3) Find the smallest element in the suffix such that array[e] < array[k]
4) swap the value of e & k in order to ensure both the suffix and the prefix is the smallest possible
5) reverse the suffix in order to ensure that the suffix is still the smallest possible
6) return the next permutation 

"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) < 2: return []   # next permutation is not possible if the length of the initial array is less than 2
        
        index = -1                    # index of k such that array[k] < array[k+1]
        n = len(nums)                 # length of the array
        
        for i in range(1,n):          # loops over the array in order to find the k such that array[k] < array[k+1]
            if nums[i] > nums[i-1]:
                index = i-1
        
        if index == -1: return nums.reverse()       # if we cannot find k then the smallest next permutation is the reverse of the initial array
            
        index1 = 0                                  # index of a such that a is the smallest element in the suffix such that a > k
        
        for i in range(index+1, n):                 # loops over the suffix looking for a
            if nums[i] > nums[index]:
                index1 = i
                
        nums[index], nums[index1] = nums[index1], nums[index]    # swap the values of a & k in order to ensure both the prefix and the suffix are the smallest possible
        
        nums[index+1:] = reversed(nums[index+1:])                # reverse the suffix to ensure that the suffix is the smallest permutation possible
        
        return nums                                 # returns the next permutation