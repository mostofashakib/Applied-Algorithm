"""
LeetCode Problem: 560. Subarray Sum Equals K
Link: https://leetcode.com/problems/subarray-sum-equals-k/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(h)

Explanation:

If the cumulative sum(represented by sum[i]sum[i] for sum up to ith up to two indices is the same,
the sum of the elements lying in between those indices is zero. Extending the same thought further,
if the cumulative sum up to two indices say i and j are at a difference of k i.e. if sum[i] - sum[j] = ksum[i]−sum[j]=k,
the sum of elements lying between indices i and j is k. Based on these thoughts,
we make use of a hashmap which is used to store the cumulative sum up to all the indices possible along with the number of times the same sum occurs.
We store the data in the form: (sum_i, no. of occurrences of sum_i). We traverse over the array nums and keep on finding the cumulative sum.
Every time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum. If the same sum occurs again,
we increment the count corresponding to that sum in the hashmap. Further, for every sum encountered,
we also determine the number of times the sum sum-ksum−k has occurred already since it will determine the number of times a subarray with sum k has occurred up to the current index.
We increment the count by the same amount.

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        hashmap[0] = 1
        runningTotal = 0
        result = 0
        
        for i in range(len(nums)):
            runningTotal += nums[i]
            
            if (runningTotal - k) in hashmap:
                result = result + hashmap[runningTotal-k]
                
            if runningTotal not in hashmap:
                hashmap[runningTotal] = 1
            else:
                hashmap[runningTotal] += 1
        
        return result
                