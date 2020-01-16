"""
LeetCode Problem: 277. Find the Celebrity
Link: https://leetcode.com/problems/find-the-celebrity/
Language: Python
Written by: Mostofa Adib Shakib

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

"""

"""
Naive Solution - Time Limited Exceeded

Time Complexity = O(n^2)
Space Complexity = O(n)
"""

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = []
        
        
        # checks for potential celebrity
        
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and knows(i, j) == False:
                    count += 1
                    if count == n-1:
                        celebrity.append(i)
        
        # if more then one celebrity exists then validate celebrity
        
        if len(celebrity) >= 0:
            if len(celebrity) == n or len(celebrity) == 0:
                return -1
            else:
                for i in range(n):
                    if i in celebrity:
                        continue
                    else:
                        for j in celebrity:
                            if knows(i, j) == False:
                                index = celebrity.pop(celebrity.index(j))
                                
        if len(celebrity) == n or len(celebrity) == 0:
                return -1
        
        return celebrity[0]

"""
Two Observations:
1) If person A knows person B then person A cannot be the celebrity and person B can potentially be the celebrity.
2) If person A does not know person B then B cannot be the celebrity and person A can potentially be the celebrity.

Time Compplexity = O(n)
Space Complexity = O(1)

"""

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        
        # checks for potential candidates
        
        for i in range(1, n):
            if knows(candidate, i) == True:
                candidate = i
                
        # checks to see if the candidate knows anyone.
        
        for i in range(0, candidate):
            if knows(candidate, i) == True:
                return -1
        
        # checks to see if anyone knows the candidate.
        
        for i in range(candidate+1, n):
            if knows(i, candidate) == False:
                return -1
            
        return candidate