"""
LeetCode Problem: 997. Find the Town Judge
Link: https://leetcode.com/problems/find-the-town-judge/
Language: Python
Written by: Mostofa Adib Shakib
"""


"""
Observations:
1) If everyone knows person A and person A doesn't know anyone then person A is a judge.
2) If the town has no population then the judge cannot be present
3) if the population of the town is 1 then it is the judge.
4) If the population of the town is equal to number of entries in trust then everyone
trusts each other and the judge can not be present.

Hashmap Solution - Fast Solution

Time Complexity = O(n)
Space Complexity = O(n)
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        # Edge cases

        if N < 0: return -1
        
        if N == 1 and len(trust) == 0: return 1
        
        if len(trust) < N - 1: return -1
        
        hashmap = {}  # A hashtable who is known by who
        guess = {}    # A hashtable that keeps that of who knows who
        

        # populates value for both the hashtables

        for i in trust:
            if i[1] not in hashmap:
                hashmap[i[1]] = [i[0]]
            else:
                hashmap[i[1]].append(i[0])
                
            if i[0] not in guess:
                guess[i[0]] = [i[1]]
            else:
                guess[i[0]].append(i[1])
                
        for key, value in hashmap.items():
            # If everyone knows an individual and the individual doesn't know anyone then we have found the judge.
            if len(value) == N-1 and key not in guess:
                return key
            
        return -1 # if there is no judge in the town


"""
Naive algorithm

Time Compplexity = O(n^2)
Space Complexity = O(1)
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if N < 0: return -1
        
        if N == 1 and len(trust) == 0: return 1
        
        hashmap = {}
        guess = []
        
        for i in trust:
            if i[1] not in hashmap:
                hashmap[i[1]] = [i[0]]
            else:
                hashmap[i[1]].append(i[0])
        
        for key, value in hashmap.items():
            if len(value) == N-1:
                guess.append(key)
                        
        for key, value in hashmap.items():
            if len(value) > 0:
                for i in value:
                    if i in guess and len(guess) > 0:
                        guess.pop()
        
        return guess[0] if len(guess) > 0 else -1