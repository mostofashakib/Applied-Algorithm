"""
LeetCode Problem: 697. Degree of an Array
Link: https://leetcode.com/problems/degree-of-an-array/
Language: Python
Written by: Mostofa Adib Shakib

This solution uses dictionary and set to find a easy and efficient solution.
"""

# Solution 1

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hashmap = {}                    # A hashmap that stores the last index of each character
        freq = {}                       # A hashmap that calculates the frequency of each character
        length = len(nums)              # Calculates the length of the array
        minimumLength = float('inf')
        visited = set()                 # Initializes a visited array to keep track of which num has been processed
        
        # Precomputer the ending index of each character in the string
        for i in range(length):
            hashmap[nums[i]] = i
        
        # Calculate the frequency of each character in a string
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        # Calculates the highest frequency
        maxFreq = max(freq.values())
        
        # Stores all keys that have the same highest frequency
        maybe = {}
        
        for key, value in freq.items():
            if value == maxFreq:
                maybe[key] = 1
        
        # Calculates the smallest possible length of a contiguous subarray of nums
        for i in range(length):
            val = nums[i]
            
            if val in maybe and val not in visited:
                visited.add(val)
                minimumLength = min(hashmap[val] - i + 1, minimumLength)
                
        
        return minimumLength
        
                
# Solution 2

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = dict()
        
        nums_set = set(nums)
        if len(nums) == len(nums_set):   # This line checks if all the elements in the input list are unique or not.
            return 1
        
        def helper(maximum, nums):                  # This is a helper function which returns the difference between the starting, ending position
            starting_index = -sys.maxsize -1        # of an element in a list and it's absolute difference.
            ending_index = -sys.maxsize -1
            for i in range(len(nums)):
                x = nums[i]
                if x == maximum:
                    starting_index = i
                    break
            for i in range(len(nums)-1, -1, -1):
                x = nums[i]
                if x == maximum:
                    ending_index = i
                    break
            IndexDiff = abs(starting_index - (ending_index+1))
            return IndexDiff
        
        for i in range(len(nums)):             # This loop populates the dictionary in order to find the elements with the maximum frequency
            x = nums[i]
            if x not in count.keys():
                count[x] = 1
            else:
                count[x] += 1
                
        maximum = [k for k,v in count.iteritems() if v == max(count.values())]  # This returns a list of elements which have the same maximum frequency
        length = len(maximum)
        
        if length >= 2:                       # This function returns the minimum possible difference between elements of the same maximum frequency
            MinSoFar = sys.maxsize
            for i in maximum:
                ans = helper(i, nums)
                if MinSoFar > ans:
                    MinSoFar = ans
            ans = MinSoFar        
        else:
            ans = helper(maximum[0], nums)
        return ans