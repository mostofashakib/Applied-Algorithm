"""
LeetCode Problem 1232. Check If It Is a Straight Lin
Link: https://leetcode.com/problems/check-if-it-is-a-straight-line/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""
A straight line consist of at least two points
If two points are connected together then it will always be a straight line
points in the same straight line has the same gradient
if the denominator of two points is zero then it is impossible
to form a straight line hence return False.
if every two contiguous points have the same gradient then return True

gradient = (y2-y1)/(x2-x1)

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) < 2: return False
        
        if len(coordinates) == 2: return True
        
        if (coordinates[1][0] - coordinates[0][0]) != 0:
            gradient = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        else:
            return False
        
        for i in range(2, len(coordinates)):
            if (coordinates[i][0] - coordinates[i-1][0]) != 0:
                count = (coordinates[i][1] - coordinates[i-1][1])/(coordinates[i][0] - coordinates[i-1][0])
            else:
                return False
            
            if count == gradient:
                continue
                
            else:
                return False
            
        return True