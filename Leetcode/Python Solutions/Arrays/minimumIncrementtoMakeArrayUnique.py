"""
LeetCode Problem: 945. Minimum Increment to Make Array Unique
Link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(NLogN)
Space Complexity: O(1)
"""

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A) <= 1:
            return 0
        
        A = sorted(A)
        count = 0
        
        for i in range(1, len(A)):
            cur = A[i]
            prev = A[i-1]
            
            if prev >= cur:
                A[i] = prev + 1
                count += prev - cur + 1
                        
        return count