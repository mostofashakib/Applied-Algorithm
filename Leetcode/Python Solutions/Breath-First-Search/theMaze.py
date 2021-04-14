"""
LeetCode Problem: 490. The Maze
Link: https://leetcode.com/problems/the-maze/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(mn)
Space Complexity: O(mn)
"""

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        numOfRows = len(maze)
        numOfCols = len(maze[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = [(start[0], start[1])]
        
        while queue:
            x, y = queue.pop(0)
            
            if [x, y] == destination:
                return True
            
            for direct in directions:
                r = x + direct[0]
                c = y + direct[1]
                
                # Keep moving until you encounter a wall
                while r >= 0 and c >= 0 and r < numOfRows and c < numOfCols and maze[r][c] == 0:
                    r += direct[0]
                    c += direct[1]
                
                # We revert one step since right now the (r, c) is a wall
                r -= direct[0]
                c -= direct[1]
                
                if (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c))
                    
        return False