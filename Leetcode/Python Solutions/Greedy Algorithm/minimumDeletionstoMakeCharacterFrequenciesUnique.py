"""
LeetCode Problem 1647. Minimum Deletions to Make Character Frequencies Unique
Link: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

class Solution:
    def minDeletions(self, s: str) -> int:
        hashmap = {}
        
        # Making a freqency table of each character
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
                
        result = 0
        sortedArray = sorted(hashmap.items(), key = lambda x:x[1])
        length = len(sortedArray)
        queue = []  
        
        for i in range(1, length):
            if sortedArray[i-1][1] == sortedArray[i][1]:
                queue.append(sortedArray[i][0])      
        
        while queue:
            element = queue.pop(0)
            freqCount = hashmap[element]
            
            while freqCount in hashmap.values() and freqCount > 0:
                result += 1
                freqCount -= 1
            
            hashmap[element] = freqCount
            
        return result