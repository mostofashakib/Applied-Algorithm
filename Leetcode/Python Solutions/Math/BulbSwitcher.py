"""
LeetCode Problem 319. Bulb Switcher

Link: https://leetcode.com/problems/bulb-switcher/
Written by: Mostofa Adib Shakib
Language: Python

Explanation:

    Notice the pattern:
    n = 1-3 -> ans = 1, diff = 2
    n = 4-8 -> ans = 2, diff = 4
    n = 9-15 -> ans = 3, diff = 6
    n = 16-24 -> ans = 4, diff = 8
    n = 25-35 -> ans = 5, diff = 10
    n = 36-48 -> ans = 6, diff = 12
    
    If there is at least one bulb then the answer is at least 1
    The difference increases by 2 after each cycle
    If the number n falls inside the range(X,Y) then the answer is equal to the answer calculated for that given range
    
    Formula needed for this problem:
    newIntDifference = PreviousIntDifference + 2
    New_Last_Position = Previous_Last_Position + 1 + newIntDifference

Complexity Analysis:
    Time Complexity: O(n)
    Space Complexity: O(1)
"""

class Solution:
    def bulbSwitch(self, n: int) -> int:
        
        # edge case
        if n == 0: return 0  # if there are no bulbs
        
        ans = 1    # keeps track of the answer
        Intdifference = 2  # keeps track of the difference
        lastPosition = 3   # the upperbound of a given range
        
        while lastPosition < n:
            lastPosition = lastPosition + 1 + (Intdifference + 2)
            Intdifference = Intdifference + 2   # in every cycle the difference increases by 2
            ans += 1       # increment answer by 1 for every cycle
            
        return ans