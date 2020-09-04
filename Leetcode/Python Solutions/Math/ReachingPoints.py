"""
LeetCode Problem: 780. Reaching Points
Link: https://leetcode.com/problems/reaching-points/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(max(tx,ty))
Space Complexity: O(1)
"""

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # If tx is smaller than sx or if ty is smaller than sy, then there is no point in calculating as the answer would be False
        if sx > tx or sy > ty:
            return False
        
        if sx == tx:
            return (ty-sy)%sx == 0 # only change y
        
        if sy == ty:
            return (tx-sx)%sy == 0
        
        if tx > ty:
            return self.reachingPoints(sx, sy, tx%ty, ty) # make sure tx%ty < ty
        
        elif tx < ty:
            return self.reachingPoints(sx, sy, tx, ty%tx)
        else:
            return False