"""
LeetCode Problem: 1274. Number of Ships in a Rectangle
Link: https://leetcode.com/problems/number-of-ships-in-a-rectangle/
Further Reading: https://leetcode.com/problems/number-of-ships-in-a-rectangle/discuss/440773/python-divide-and-conquer-with-picture-explanation?fbclid=IwAR3bbeab1OqVEIxXGwD4Zu28JIh448PmaaqMX52rUwVkOuloJQN-x_cU040

Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def helper(P, Q):
            if Q.x > P.x or Q.y > P.y:
                return 0
            
            elif (P.x, P.y) == (Q.x, Q.y):
                return int(sea.hasShips(P, Q))
            
            elif not sea.hasShips(P, Q):
                return 0
            
            else:
                midX = (P.x + Q.x)//2
                midY = (P.y + Q.y)//2
                
                f1 = helper(Point(midX, P.y), Point(Q.x ,midY+1))
                f2 = helper(P, Point(midX+1,midY+1))
                f3 = helper(Point(midX, midY), Q)
                f4 = helper(Point(P.x, midY), Point(midX+1, Q.y))
                
                return f1 + f2 + f3 + f4
            
        return helper(topRight, bottomLeft) 