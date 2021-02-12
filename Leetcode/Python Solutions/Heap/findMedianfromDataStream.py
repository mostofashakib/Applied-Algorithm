"""
LeetCode Problem: 295. Find Median from Data Stream
Link: https://leetcode.com/problems/find-median-from-data-stream/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(log n)
Space Complexity: O(n)
"""

import heapq 

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.upperHalf = []   # min heap
        self.lowerHalf = []   # max heap
        self.numCount = 0     # Count of the total number of numbers seen from the data stream
        
    # A helper function that adds a given value to the correct heap
    def addToHeap(self, val):
        # Push the current value if it is less than the maximum value in the lower half
        if not self.lowerHalf or val < -self.lowerHalf[0]:
            heapq.heappush(self.lowerHalf, -val)
        else:
            heapq.heappush(self.upperHalf, val)
    
    #  A helper function which ensures that the size difference between the two heaps is at most 1
    def reBalanceTheHeap(self, val):
        if len(self.lowerHalf) > len(self.upperHalf) + 1:
            num = heapq.heappop(self.lowerHalf)
            heapq.heappush(self.upperHalf, -num)
            
        elif len(self.upperHalf) > len(self.lowerHalf) + 1:
            num = heapq.heappop(self.upperHalf)
            heapq.heappush(self.lowerHalf, -num)
            
    def addNum(self, num: int) -> None:
        self.addToHeap(num)
        self.reBalanceTheHeap(num)
        self.numCount += 1
      
    def findMedian(self) -> float:
        
        # Checks to see if the heap is of odd length
        if self.numCount % 2 != 0:
            if len(self.lowerHalf) > len(self.upperHalf):
                return -self.lowerHalf[0]
            else:
                return self.upperHalf[0]
            
        return float( (-self.lowerHalf[0]+self.upperHalf[0]) /2.0) 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()