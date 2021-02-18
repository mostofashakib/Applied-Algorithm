"""
LeetCode 532. K-diff Pairs in an Array
Link: https://leetcode.com/problems/k-diff-pairs-in-an-array/
Language: Python3
Written by: Mostofa Adib Shakib
"""

# Efficient - HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        hashmap = {}
        
        # populating a frequency table
        for elem in nums:
            if elem not in hashmap:
                hashmap[elem] = 1
            else:
                hashmap[elem] += 1
        
        # walk through the items in the hashmap
        for key, value in hashmap.items():
        	# if the difference is greater than 0 then check to see if the (key+k)th element exists in the hashmap or not
            if k > 0 and key+k in hashmap:
                result += 1

            # if the difference is 0 then check if the element occurs at least twice or not
            elif k == 0 and value > 1:
                result += 1
        
        return result

# Optimized Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
    	n = len(nums)
        result = set()
        nums = sorted(nums)
        
        for i in range(n):
            for j in range(i+1, n):
            	# If the difference is greater than k then no point in looking to the right in a sorted array
                if abs(nums[i] - nums[j]) > k:
                    break
                    
                if abs(nums[i] - nums[j]) == k:
                    if (nums[i], nums[j]) not in result and (nums[j], nums[i]) not in result:
                        result.add((nums[i], nums[j]))
        
        return len(result)