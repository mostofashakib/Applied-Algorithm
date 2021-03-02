"""
LeetCode Problem: 1010. Pairs of Songs With Total Durations Divisible by 60
Link: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        array = [0] * 60
        
        for v in time:
            array[v % 60] += 1
                
        for i in range(1, 30):
            count += array[i] * array[60 - i]
                        
        for i in [0, 30]:
            count += (array[i] - 1) * array[i] // 2
            
        return count