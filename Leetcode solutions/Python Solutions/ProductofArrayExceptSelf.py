"""
LeetCode Problem: 238. Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/
Language: Python
Written by: Mostofa Adib Shakib

Two solutions:

1) Efficient
2) Brute Force algorithm

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer


"""

Brute Force solution using a matrix.

The brute force solution is pretty intuitive. 

Brute Force algorithm:

1) We initialize a 2-D array and assign all the diagonal elements to be 1.
2) We assign all the other elements in each row and multiply all the elements in the same row to get their product

Time complexity = O(n^2)
Space complexity = O(n^2)

"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        matrix = [ [ float('-inf') for i in range(len(nums))] for i in range(len(nums)) ]
        result = []
        
        for coloumn in range(len(matrix)):
            for row in range(len(matrix[0])):
                if coloumn == row:
                    matrix[row][coloumn] = 1
                else:
                    matrix[row][coloumn] = nums[coloumn]
        
        def prod(array):
            if len(array)==0: return 1
            else: return array[0]*prod(array[1:])
            
        for i in matrix:
            result.append(prod(i))
            
        return result