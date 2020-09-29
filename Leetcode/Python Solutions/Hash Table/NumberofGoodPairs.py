"""
LeetCode Problem: 1512. Number of Good Pairs
Link: https://leetcode.com/problems/number-of-good-pairs/
Reading Material: https://stackoverflow.com/questions/18859430/how-do-i-get-the-total-number-of-unique-pairs-of-a-set-in-the-database#:~:text=Since%20every%20pair%20is%20counted,9900%2F2%20%3D%204950)

Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)

Formula to calculate the number of unique pairs for a given number:

No. of Unique pairs = n*(n-1)//2
"""

# Optimal

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        count = 0
        
        for index, key in enumerate(nums):
            if key not in hashmap:
                hashmap[key] = 1
            else:
                hashmap[key] += 1
        
        for value in hashmap.values():
            if value > 1:
                count += value*(value-1)//2
                
        return count

# Brute Force

from itertools import permutations 

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        count = 0
        
        for index, key in enumerate(nums):
            if key not in hashmap:
                hashmap[key] = [index]
            else:
                hashmap[key].append(index)
                
        for key, value in hashmap.items():
            if len(value) > 1:
                perm = permutations(value, 2)   # generates all permutations of array length 2
                count += len(list(perm))
                
        return count//2