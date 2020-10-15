"""
LeetCode Problem: 1296. Divide Array in Sets of K Consecutive Numbers
Link: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity : O(Nlog(N))
Space complexity : O(n)

Greedy Approach:

We first sort the given input array and populate a hashmap in order to count the frequency of each number in the input array.

After the hashmap has been populated we grab one key at a time and check if the number is still present in the sorted array.
If so we check to see if we can form a set of k consecutive numbers from a given key and decrement the frequency of each of those
k consecutive numbers by 1. However, if we cannot form a set of k consecutive numbers then we return False.
"""

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        hashmap = {} # initializing  a hashmap
        
        nums = sorted(nums)   # sorting the input array
        
        # populating a hashmap
        
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        for key in hashmap.keys():
            while hashmap[key] > 0:
                # checks for all possible subarrays that can be constructed from a given key
                for value in range(key, key+k):
                    # checks if the value exists in the hashmap and the current occurrence
                    if value in hashmap and hashmap[value] > 0:
                        hashmap[value] -= 1
                    else:
                        return False
        return True