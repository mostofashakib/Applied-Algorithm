"""
LeetCode Problem: 767. Reorganize String
Link: https://leetcode.com/problems/reorganize-string/
Language: Python
Written by: Mostofa Adib Shakib

"""

# Brute-Force Solution - Time Limit Exceeded
# Generate all permutations of the given string and check if it has unique adjacent characters
# Time Complexity: 
# Space Complexity: 

from itertools import permutations 

class Solution:
    def reorganizeString(self, S: str) -> str:
        
        def checker(S):
            for i in range(1, len(S)-1):
                if S[i-1] != S[i] != S[i+1]:
                    if i == len(S)-2:
                        return S
                else:
                    break

            return ""
        
        perm = permutations(S)
        
        for i in list(perm):
            string = ''.join(i)
            
            if checker(string) != "":
                return string
            
        return ""



# Efficient Solution - Greedy with Heap
# Time Complexity:  O(NlogA) where N is the length of S, and A is the size of the alphabet. If A is fixed, this complexity is O(N)
# Space Complexity: O(A). If A is fixed, this complexity is O(1).

import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        
        # edge cases

        if not S or len(S) == 1:
            return S
        
        # make a heap
        counts = Counter(S)
        heap = [(-v, k) for k, v in counts.items()]   # makes it a maxHeap
        heapq.heapify(heap)
        
        # construct ans
        ans = ""
        
        while len(heap) > 1:
            count1, c1 = heapq.heappop(heap)
            count2, c2 = heapq.heappop(heap)
            
            ans += c1 + c2
            
            count1 += 1
            count2 += 1
            
            if count1 < 0:
                heapq.heappush(heap, (count1, c1))
                
            if count2 < 0:
                heapq.heappush(heap, (count2, c2))  
                    
        if heap:
            count, c = heapq.heappop(heap)
            if count < -1:
                return ""
            else:
                ans += c
        
        return ans