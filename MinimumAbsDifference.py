"""
1200 Leetcode: Minimum absolute difference
https://leetcode.com/problems/minimum-absolute-difference/
"""


"""
We sort an array at the beginning and they loop over till the second last index of the array. We compare the first element with the second element 
and compare the difference with the tracker which has the maximum size of an integer. If the difference is smaller then change the value
of the tracker and append the subarray to a resulting array. Keep doing it for all the subarrays whose difference is also the minimum
and return the result.
"""

def minimumAbsDifference(self, arr):
    """
    :type arr: List[int]
    :rtype: List[List[int]]
    """
    A = sorted(arr)
    result = []
    minimum = float('inf')
    for i in xrange(len(A)-1):
        min_d = A[i+1] - A[i]
        if min_d < minimum:
            minimum = min_d
            result.append([A[i], A[i+1]])
        elif min_d == minimum:
            result.append([A[i], A[i+1]])
    return result
