"""
LeetCode Problem: 1297. Maximum Number of Occurrences of a Substring
Link: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Brute Force Solution
# Time Complexity: O(n*m)
# Space Complexity: O(n)

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        hashmap = {}
        length = len(s)
        
        for size in range(minSize, maxSize+1):
            for i in range(length-size+1):
                subString = s[i:i+size]
                
                if len(set(subString)) <= maxLetters:
                    if subString not in hashmap:
                        hashmap[subString] = 1
                    else:
                        hashmap[subString] += 1
        
        return 0 if not hashmap else max(hashmap.values())

# Optimal Solution
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        maps = {}
        n = len(s)
        res = 0
        
        for i in range(n-minSize+1):
            sub = s[i:i+minSize]
            if len(set(sub)) < =maxLetters:
                # if the key does not exist then it returns 0
                maps[sub] = maps.get(sub,0) + 1
                res = max(res, maps[sub])
        return res