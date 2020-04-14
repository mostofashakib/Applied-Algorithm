"""
LeetCode Problem 1046. Last Stone Weight
Link: https://leetcode.com/problems/last-stone-weight/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""
Approach 1
Time Complexity: O(nlogn)
Space Complexity: O(1) In Python, converting a list to a heap is done in-place, requiring O(1)O(1) auxillary space,
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # converts max heap to min heap
        
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
        
        length = len(stones)
        
        while length > 1:
            FirstHighest = heapq.heappop(stones)
            SecondHighest = heapq.heappop(stones)
            
            if FirstHighest == SecondHighest:
                length -= 2
            
            else:
                newElement = FirstHighest - SecondHighest
                heapq.heappush(stones,newElement)
                length -= 1
        
        if len(stones) == 0: return 0
        
        return -stones[0]
                

"""
Approach 2:
Time Complexity: O(n*mlogn)
Space Complexity: O(1)
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones, reverse = True)
        length = len(stones)
        
        while length > 1:
            FirstHighest = stones[0]
            SecondHighest = stones[1]
            
            if FirstHighest == SecondHighest:
                stones.pop(0)
                stones.pop(0)
                length -= 2
            
            else:
                newElement = FirstHighest - SecondHighest
                stones[0] = newElement
                stones.pop(1)
                stones = sorted(stones, reverse = True)
                length -= 1
                
        if len(stones) == 0: return 0
        
        return stones[0]
