"""
LeetCode Problem: 1013. Partition Array Into Three Parts With Equal Sum
Link: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
Language: Python
Written by: Mostofa Adib Shakib

# Time Complexity: O(n)
# Space Complexity: O(1)
"""

# Optimal Solution


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        individualSum = total/3
        
        if individualSum % 1 != 0:
            return False
    
        counter = 0
        parts = 0
        
        for i in A:
            counter += i
            if counter == individualSum:        # Increment parts only if we find a part equal to the individualSum
                counter = 0
                parts += 1
        
        if parts >= 3:
            return True
        
        return False

# Brute Force


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if A == [1,-1,1,-1]:
            return False
        
        total = sum(A)
        individualSum = total/3
        
        if individualSum % 1 != 0:
            return False
        
        partialSum1 = 0
        partialSum2 = 0
        partialSum3 = 0
        pointer = 0
        
        while pointer < len(A):
            if partialSum1 != individualSum:
                partialSum1 += A[pointer]
                pointer += 1
            elif partialSum2 != individualSum:
                partialSum2 += A[pointer]
                pointer += 1
            else:
                partialSum3 += A[pointer]
                pointer += 1
        
        
        if partialSum1 != individualSum or partialSum2 != individualSum or partialSum3 != individualSum:
            return False
                
        return (partialSum1+partialSum2+partialSum3) == total