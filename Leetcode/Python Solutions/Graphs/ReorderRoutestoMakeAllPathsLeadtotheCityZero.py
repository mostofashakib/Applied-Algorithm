"""
LeetCode Problem: 1466. Reorder Routes to Make All Paths Lead to the City Zero
Link: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        # building the graph
        for u, v in connections:
            graph[u].append((v, 1))     # outgoing edge
            graph[v].append((u, 0))     # incoming edge
            
        ans = 0
        queue = [0]
        visited = set([0])
        
        while queue:
            curr_city = queue.pop(0)
            
            for neighbor, weight in graph[curr_city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    ans += weight
                    queue.append(neighbor)
        return ans