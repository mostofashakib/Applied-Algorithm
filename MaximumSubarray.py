""" 
LeetCode Problem: 53. Maximum Subarray
Link: https://leetcode.com/problems/maximum-subarray/
Language: Python
Written by: Mostofa Adib Shakib

"""

"""

Brute force solution 1
Time complexity: O(n^3)

We use two loops one starts from the first index of the array and the other one starts from the last index of the arrray. We also use a third inner loop in order to calculate
the sum of all the elements inside the two outerloops. We keep track of the running window sum and take the maximum value of the current running window sum and the maximum value
seen so far.

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        MaxSeenSofar = float('-inf')
        n = len(nums)
        
        for i in range(0, n, 1):
            for j in range(n, 0, -1):
                windowSum = 0
                
                for k in range(i, j):
                    windowSum += nums[k]
                
                MaxSeenSofar = max(MaxSeenSofar, windowSum)
                
        return MaxSeenSofar


"""

Brute force solution 2
Time complexity: O(n^2)

In this second brute force solution we use two loops. The outloop loops over all the element one by one and the inner loop calculates the window running total.
We keep track of the running window sum and take the maximum value of the current running window sum and the maximum value
seen so far.

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        MaxSeenSoFar = float('-inf')
        n = len(nums)
        
        
        for i in range(0, n):
            runningWindowSum = 0
            for j in range(i, n):
                runningWindowSum += nums[j]
                MaxSeenSoFar = max(MaxSeenSoFar, runningWindowSum)
            
        return MaxSeenSoFar


"""

Dynamic Programming(Kadane's Algorithm)
Time Complexity: O(n)
Space complexity: O(n)

In this solution we loop over an array one time and build up the MaxSeenArray array. 
The core concept is to compare the current element with the MaxSeen so far added with the current element
and take the maximum each time. This results in a global maximum value.

"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MaxSeenArray = [0 for i in range(n)]
        MaxSeenArray[0] = nums[0]
                
        for i in range(1, n):
            MaxSeenArray[i] = max(nums[i], nums[i] + MaxSeenArray[i-1])
        
        return max(MaxSeenArray)