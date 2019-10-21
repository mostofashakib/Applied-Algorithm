"""
941 Leetcode. Valid Mountain Array
https://leetcode.com/problems/valid-mountain-array/
"""

"""

This is solution we use assign a pointer and a variable with the length of the array.
At first we run a while loop for the strickly increasing part and increment the pointer each time. If the pointer value is equal
to the length of the array or 0 that means either the array wasn't strictly increasing or is only strickly increasing hence we return False.
If the value of i is still less than the length of the array then we go to the second while loop and increment the pointer for the 
strickly decreasing part. At the end we check if the value of the pointer is the same as the length of the array. If they are equal
then we return True as the array is a mountain array or else we return False. 

"""

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A) -1 
        i = 0
        
        while i < length and A[i] < A[i+1]:
            i += 1

        if i == 0 or i == length:
            return False
            
        while i < length and A[i] > A[i+1]:
            i += 1
        return i == length