"""
LeetCode Problem: 1326. Minimum Number of Taps to Open to Water a Garden
Link: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Greedy Solution - Varient of Jump Game
# Time Complexity: 
# Space Complexity: 


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        if not ranges:
            return -1
        
        jump_distance = [0] * (n + 1)
        
        for index, radius in enumerate(ranges):
            left, right = max(0, index - radius), min(n, index + radius)
            jump_distance[left] = max(jump_distance[left], right - left)
            
        jump_count = 0
        cur_range = -1
        next_range = 0
        
        for position, distance in enumerate(jump_distance):
            # check if a position is not within the current jump range
            if position > cur_range:
                # if a position is not within reach terminate early
                if position > next_range:
                    return -1
                
                # add a jump and move the current jump range end to the cached next_range
                jump_count += 1
                cur_range = next_range
            
            # update the next range if the current distance is an improvement in range
            next_range = max(next_range, position + distance)
        
        return jump_count - 1


# Dynamic Programming
# Time Complexity: 
# Space Complexity: 

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        res=[]
        for i in range(len(ranges)):
            res.append([i-ranges[i],i+ranges[i]])
        
        res.sort(key = lambda x:x[0])
        dp=[float('inf') for i in range(n+1)]
        dp[0]=0
        
        for i in res:
            leftBound = max(0, i[0])
            rightBound = min(i[1] + 1, n+1)
            
            for j in range(leftBound, rightBound):
                if dp[j] == float('inf') and i[0] < 0:
                    dp[j] = dp[0] + 1
                elif dp[j] == float('inf') and j > 0:
                    dp[j] = dp[i[0]] + 1
        
        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]