"""
LeetCode Problem: 480. Sliding Window Median
Link: https://leetcode.com/problems/sliding-window-median/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(nlogk)
Space Complexity: O(N)
"""

class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        
    def balance(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def addNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        self.balance()
        
    def removeNum(self, num):
        if num <= -self.maxHeap[0]:
            self.maxHeap.remove(-num)
            heapq.heapify(self.maxHeap)
        else:
            self.minHeap.remove(num)
            heapq.heapify(self.minHeap)
            
        self.balance()

    def findMedian(self, k):
        if k % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return -self.maxHeap[0]

class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        
        start = 0
        end = 0
        mf = MedianFinder()
        length = len(nums)
        result = []
        
        while end < length:
            mf.addNum(nums[end])
            
            if end >= k-1:
                result.append(mf.findMedian(k))
                mf.removeNum(nums[start])
                start += 1
            end += 1
            
        return result