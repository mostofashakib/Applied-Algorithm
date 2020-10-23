"""
LeetCode Problem 763. Partition Labels
Link: https://leetcode.com/problems/partition-labels/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        hashmap = {}                    # Initializing an hashmap to store the last occurence of every alphabet
        length = len(S)
        startingIndex = 0               # Keeping track of the starting point of the partition
        endingIndex = 0                 # Keeping track of the ending point of the partition
        result = []                     # Initializing an array for storing results
        
        # Precomputing the last occurence of every character
        
        for i in range(length):
            hashmap[S[i]] = i
        

        for index in range(length):
            endingIndex = max(endingIndex, hashmap[S[index]])     # The endingIndex is the last most occurence of an alphabet in a given partition
            
            if index == endingIndex:                              # This is only true if we have found a partition
                result.append(endingIndex-startingIndex+1)        # We increment the difference by 1 since the array is 0 indexed
                startingIndex = endingIndex + 1
        
        return result