"""
LeetCode Problem: 934. Shortest Bridge
Link: https://leetcode.com/problems/shortest-bridge/
Written by: Mostofa Adib Shakib
Language: Python

Explanation:
	1) Find the coordinate of a point that is a part of an island.
	2) Using Depth-First Search turn every point that is part of the first island to 2 and add the coordinate to the visited set and the deque.
	3) Using Breath-First Search find the shortest path from the first island to the second island.
	4) Once any point that is part of the second island is found we stop the algorithm and return the coordinate

Time Complexity: O(R * C)
Space Complexity: O(R * C)
"""

class Solution:
		def shortestBridge(self, A: List[List[int]]) -> int:     
			def dfs(r, c):
				if r < 0 or c < 0 or r >= len(A) or c >= len(A[0]) or A[r][c] == 0 or A[r][c] == 2:
					return

				A[r][c] = 2
				visited.add((r, c))
				queue.append((r, c, 0))

				dfs(r + 1, c)
				dfs(r - 1, c)
				dfs(r, c + 1)
				dfs(r, c - 1)

			visited = set()
			queue = deque([])
			numRows = len(A)
			numCols = len(A[0])
			directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
			flag = False

			for r in range(numRows):
				for c in range(numCols):
					if A[r][c] == 1:
						dfs(r, c)
						flag = True
						break

				if flag == True:
					break

			while queue:
				r, c, steps = queue.popleft()

				if A[r][c] == 1:
					return steps - 1

				for direct in directions:
					row = r + direct[0]
					col = c + direct[1]

					if row >= 0 and col >= 0 and row < numRows and col < numCols and (row, col) not in visited:
						visited.add((row, col))
						queue.append((row, col, steps + 1))