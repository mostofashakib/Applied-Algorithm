"""
This program uses recursion to sort an array in O(nlong) time. We take the pivot as the middle most element in the array then we
recursively sort the left and right half of the array. We return the array if the length of the array is one of less as there is only one element.
"""

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def quickSort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr)//2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quickSort(left) + middle + quickSort(right)
        
        return quickSort(nums)