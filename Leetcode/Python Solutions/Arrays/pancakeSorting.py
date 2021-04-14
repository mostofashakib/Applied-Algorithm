"""
LeetCode Problem: 969. Pancake Sorting
Link: https://leetcode.com/problems/pancake-sorting/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N^2)
Space Complexity: O(N)
"""

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # If the array size is 1 then it's already sorted
        if len(arr) == 1:
            return arr
        
        # A helper function that flips the first K elements of the array
        def flip(arr, k):
            first = 0
            last = k
            
            while first < last:
                arr[first], arr[last] = arr[last], arr[first]
                first += 1
                last -= 1
        
        # A helper function that find the index of the maximum element from the top k elements
        def findMaximumIndex(k):
            maximumValue = float('-inf')
            maximumIndex = 0
            
            for j in range(k):
                if arr[j] > maximumValue:
                    maximumValue = arr[j]
                    maximumIndex = j
            
            return maximumIndex
        
        k = len(arr) - 1
        result = []
        
        while k > 0:
            maximumIndex = findMaximumIndex(k+1)
            
            # If the element to be swapped is already in the right position
            if maximumIndex == k:
                k -= 1
                continue
            
            # If the element to be swapped is not the top element then flip it to the head
            if maximumIndex != 0:
                result.append(maximumIndex+1)
                flip(arr, maximumIndex)
                
            result.append(k+1)
            flip(arr, k)
            k-= 1
        
        return result