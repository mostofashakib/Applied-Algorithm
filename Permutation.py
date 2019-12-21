"""
46 Leetcode. Permutations
https://leetcode.com/problems/permutations/
Written by: Mostofa Adib Shakib
Language: Python
"""


"""

Algorithm:

If the first integer to consider has index n that means that the current permutation is done.

Iterate over the integers from index first to index n - 1.
    Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
    Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
    Now backtrack, i.e. swap(nums[first], nums[i]) back.

Time Complexity: O(n*n!)
Note that there are n! permutations and it requires O(n) time to print a a permutation.

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        
        def all_permutations(a, l, r):
            if l == r:
                result.append(a[:])  # if we have a match then append to result
            else:
                for i in range(l, r+1): # traverse through all the characters in an array
                    a[l], a[i] = a[i], a[l] #swap two characters and recurse
                    all_permutations(a, l+1, r)  #recurse over the next fixed character
                    a[l], a[i] = a[i], a[l] #backtrack if a solution can't be found.
        
        all_permutations(nums, 0, n-1)
        
        return result