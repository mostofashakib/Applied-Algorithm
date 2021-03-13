"""
LeetCode Problem 801. Minimum Swaps To Make Sequences Increasing

Link: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
Written by: Mostofa Adib Shakib
Language: Python

Time complexity: O(n)
Space complexity: O(n)

Explanation:

1) A[i - 1] < A[i] && B[i - 1] < B[i].
    In this case, if we want to keep A and B increasing before the index i, can only have two choices.
        -> 1.1 don't swap at (i-1) and don't swap at i, we can get not_swap[i] = not_swap[i-1]
        -> 1.2 swap at (i-1) and swap at i, we can get swap[i] = swap[i-1]+1
    If swap at (i-1) and do not swap at i, we can not guarantee A and B increasing.

2) A[i-1] < B[i] && B[i-1] < A[i]
    In this case, if we want to keep A and B increasing before the index i, can only have two choices.
        -> 2.1 swap at (i-1) and do not swap at i, we can get notswap[i] = Math.min(swap[i-1], notswap[i] )
        -> 2.2 do not swap at (i-1) and swap at i, we can get swap[i]=Math.min(notswap[i-1]+1, swap[i])
"""

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        length = len(A)
        not_swap = [0] + [float('inf')] * (length-1)
        swap = [1] + [float('inf')] * (length-1)
        
        for i in range(1, length):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                swap[i] = swap[i - 1] + 1
                not_swap[i] = not_swap[i - 1]
                
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                swap[i] = min(swap[i], not_swap[i - 1] + 1)
                not_swap[i] = min(not_swap[i], swap[i - 1])
                
        return min(swap[-1], not_swap[-1])