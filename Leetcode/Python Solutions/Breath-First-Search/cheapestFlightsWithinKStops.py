"""
LeetCode Problem: 787. Cheapest Flights Within K Stops
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(K⋅E)
Space Complexity: O(V)
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        hashMap = defaultdict(list)
        
        for source, destination, cost in flights:
            hashMap[source].append((destination, cost))
        
        minimumCost = float('inf')
        queue = deque([(src, 0, -1)])
        visited = [float('inf')] * n
        
        while queue:
            node, cost, count = queue.popleft()
            
            if node == dst and count <= K:
                minimumCost = min(minimumCost, cost)
            
            if count < K:
                for nextNode, nextCost in hashMap[node]:
                    if visited[nextNode] > cost + nextCost:
                        visited[nextNode] = cost + nextCost
                        queue.append((nextNode, cost + nextCost, count + 1))
        
        return minimumCost if minimumCost != float('inf') else -1