"""
LeetCode Problem: 836. Rectangle Overlap
Link: https://leetcode.com/problems/rectangle-overlap/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rect1_x1 = rec1[0]
        rect1_y1 = rec1[1]
        rect1_x2 = rec1[2]
        rect1_y2 = rec1[3]
        
        rect2_x1 = rec2[0]
        rect2_y1 = rec2[1]
        rect2_x2 = rec2[2]
        rect2_y2 = rec2[3]
        
        if  rect1_x1 == rect1_x2 or rect1_y1 == rect1_y2 or rect2_x1 == rect2_x2 or rect2_y1 == rect2_y2:
            return False
        
        if rect1_x1 < rect2_x2 and rect1_y1 < rect2_y2 and rect2_x1 < rect1_x2 and rect2_y1 < rect1_y2:
            return True
        
        return False