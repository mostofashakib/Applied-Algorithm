"""
LeetCode Problem 875. Koko Eating Bananas

Link: https://leetcode.com/problems/koko-eating-bananas/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(nlogn)
Space complexity: O(1)
"""

class Solution:
    # A helper function that if a given K value will be enough to eat all the bananas in H hours.
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(K):
            hours = 0
            
            for p in piles:
                # The ternary is required because when we divide 5/5 expected hours required is 1 instead of 2
                hours += 1 if p == K else (p//K) + 1
            
            return False if hours > H else True     # A given K value is only valid if hours is less than or equal to H
            
        low = 1
        high = max(piles)       # Gets the maximum value from piles as K cannot be larger than the maximum value
        
        # We perform binary search to find the smallest K value possible that would suffice the given constrains
        while low <= high:
            mid = (high+low)//2
            
            if possible(mid) == True:
                high = mid - 1
            else:
                low = mid + 1
        
        return low