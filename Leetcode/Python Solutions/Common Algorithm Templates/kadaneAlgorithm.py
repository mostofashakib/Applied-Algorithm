"""
Kadane's Algorithm to find the maximum subarray sum
Written by: Mostofa Adib Shakib
Language: Python
"""

def kadaneAlgorithm(self, nums):    
    curSum = 0
    maxiSum = float('-inf')
    
    for i in range(len(nums)):
        curSum = curSum + nums[i]
        maxiSum = max(maxiSum, curSum)
            
        if curSum < 0:
            curSum = 0
    
    return maxiSum