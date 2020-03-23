"""
LeetCode Problem: 274. H-Index
Link: https://leetcode.com/problems/h-index/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n)
Space Complexity: O(1)

"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        Sarray = sorted(citations)     # sorts the array in ascending order
        n = len(Sarray)                # length of the array
        
        for key,value in enumerate(Sarray):   # loops over the array
            entry = n - key                   # keeps track of the number of citations with value greater and equal to the current citation
            if value >= entry:                # if the value of citation is greater than or equal to the entries left
                return entry                  # return the number of entry
        
        return 0                              # returns 0 if the above condition doesn't hold.
