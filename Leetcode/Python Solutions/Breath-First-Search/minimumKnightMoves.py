"""
LeetCode Problem: 1197. Minimum Knight Moves
Link: https://leetcode.com/problems/minimum-knight-moves/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O( max(x, y)^2 )
Space Complexity: O( max(x, y)^2 )
"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque([(0, 0, 0)])
        directions = [(1, 2), (-1, 2), (-2, 1), (2, 1), (2, -1), (-2, -1), (-1, -2), (1, -2)]
        visited = set()
        
        while queue:
            xCor, yCor, steps = queue.popleft()
            
            if (xCor, yCor) == (x, y):
                return steps
            
            for direct in directions:
                r = xCor + direct[0]
                c = yCor + direct[1]
                
                if (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, steps + 1))