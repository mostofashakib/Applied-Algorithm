""" 
LeetCode Problem: 1007. Minimum Domino Rotations For Equal Row
Link: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""
Inefficient - Simulation with all possible dominos
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        # Helper function that returns the minimumSwaps required for a target domino
        def dominoMinimumSwaps(target, A, B):
            minSwaps = 0
            
            for i in range(len(A)):
                if A[i] != target and B[i] != target:
                    return float('inf')
                elif A[i] != target:
                    minSwaps += 1
                    
            return minSwaps
        
        minSwaps = float('inf')
        dominoChoice = set(A).union(set(B))             # All possible domino choices
        
        # Simulate all possible domino swap combinations possible
        for i in list(dominoChoice):
            minSwaps = min(minSwaps, dominoMinimumSwaps(i, A, B))       # A specific domino can match the top row
            minSwaps = min(minSwaps, dominoMinimumSwaps(i, B, A))       # A specific domino can match the bottom row
        
        return minSwaps if minSwaps != float('inf') else -1


"""
Efficient - Simulation with selected dominos
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        # Helper function that returns the minimumSwaps required for a target domino
        def dominoMinimumSwaps(target, A, B):
            minSwaps = 0
            
            for i in range(len(A)):
                if A[i] != target and B[i] != target:
                    return float('inf')
                elif A[i] != target:
                    minSwaps += 1
                    
            return minSwaps
        
        minSwaps = float('inf')
        
        # Simulate domino swap combinations
        minSwaps = min(minSwaps, dominoMinimumSwaps(A[0], A, B))
        minSwaps = min(minSwaps, dominoMinimumSwaps(B[0], A, B))
        minSwaps = min(minSwaps, dominoMinimumSwaps(A[0], B, A))
        minSwaps = min(minSwaps, dominoMinimumSwaps(B[0], B, A))
        
        return minSwaps if minSwaps != float('inf') else -1