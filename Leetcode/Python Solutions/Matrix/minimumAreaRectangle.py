"""
LeetCode Problem: 939. Minimum Area Rectangle
Link: https://leetcode.com/problems/minimum-area-rectangle/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0
        
        ans = inf
        seen = { (x, y) for x, y in points }
        
        for x, y in points: 
            for xx, yy in points: 
                if x != xx and y != yy and (x, yy) in seen and (xx, y) in seen: 
                    ans = min(ans, abs((xx-x)*(yy-y)))
        
        return ans if ans != inf else 0