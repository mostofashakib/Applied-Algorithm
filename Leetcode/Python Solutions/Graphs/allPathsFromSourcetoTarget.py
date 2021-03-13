"""
LeetCode Problem: 797. All Paths From Source to Target
Link: https://leetcode.com/problems/all-paths-from-source-to-target/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(2^N * N)
Space Complexity: O(2^N * N)
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        length = len(graph)
        ans = []
        
        def backtrack(currNode, path, n):
            # if we reach the target, no need to explore further.
            if currNode == n:
                ans.append(path.copy())
                return
            # explore the neighbor nodes one after another.
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path, n)
                path.pop()
        
        path = [0]
        backtrack(0, path, length-1)
        return ans