"""
LeetCode Problem: 1059. All Paths from Source Lead to Destination
Link: https://leetcode.com/problems/all-paths-from-source-lead-to-destination/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(V+E)
Space Complexity: O(V+E)
"""

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        hashMap = defaultdict(list)
        
        for edge in edges:
            startVertex = edge[0]
            endVertex = edge[1]
            hashMap[startVertex].append(endVertex)
            
        if hashMap[destination]:
            return False

        def dfs(node, visited):
            if node == destination:
                return True
            
            if node in visited:
                return False
        
            jobs = []
                        
            for vertex in hashMap[node]:
                jobs.append(dfs(vertex, visited.union({node})))   
            
            return all(jobs) if jobs else False
        
        return dfs(source, set())