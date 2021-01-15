"""
LeetCode Problem: 239. Sliding Window Maximum
Link: https://leetcode.com/problems/sliding-window-maximum/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        deque = []      # Initializing deque
        result = []     # Initializing an array
        
        for i in range(len(nums)):
            # If elements at the top of the deque is outside the current window
            if deque and i - deque[0] == k:
                deque.pop(0)
            
            # If the last elements are smaller than the element being considered
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            
            deque.append(i)         # Push the index of the element to the deque
            
            # If we have one finished window
            if i+1 >= k:
                result.append(nums[deque[0]])
                
        return result