"""
LeetCode Problem: 986. Interval List Intersections
Link: https://leetcode.com/problems/interval-list-intersections/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        
        firstPointer = 0
        secondPointer = 0
        lengthA = len(A)
        lengthB = len(B)
        result = []
        localMinimum = float('-inf')
        localMaximum = float('inf')
        
        while firstPointer < lengthA and secondPointer < lengthB:
            startTimeA = A[firstPointer][0]
            endTimeA = A[firstPointer][1]
            startTimeB = B[secondPointer][0]
            endTimeB = B[secondPointer][1]   
                    
            localMinimum = max(startTimeA, startTimeB)
            localMaximum = min(endTimeA, endTimeB)

            if localMaximum >= localMinimum:
                result.append([localMinimum, localMaximum])
            
            # Remove the interval with the smallest endpoint
            if endTimeA < endTimeB:
                firstPointer += 1
            else:
                secondPointer += 1
        
        return result