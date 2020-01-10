"""
LeetCode Problem: 1192. Critical Connections in a Network
Link: https://leetcode.com/problems/critical-connections-in-a-network/
Language: Python
Written by: Mostofa Adib Shakib

"""

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # This solution uses Tarjan's algorithm to find critical connections in a graph
        # Low Link value is defined as the lowest
        
        """
        A low link value of a node is defined as the smallest rank reachable from that node.
        
        A bridge is a node in a graph whose removal increses the number of connected components
        
        Bridge = lowLink[node] > current_rank
        
        low-link value is initially equal to which number the node has during the initial DFS.
        If it's the first node visited, the value will be 0. If it's the second node, it will be 1.
        The third node has value 2, the fourth value 3, etc.

        From there, the low-link value is updated so that it tracks which SCC the given node happens to be in.
        The idea is that initially we consider each node to be in its own SCC, but then if we find that two different nodes are in the same  
        SCC, we update the low-link values of all of these nodes so that they're all the same.
        
        Tarjan's Algorithm:
        
        Start at any node and do a depth first search traversal labeling nodes with an increasing rank values as you go.
        Keep track of the rank of each node and the smallest low-link value. During the DFS, bridges will be found where the
        rank of the node your edge is coming from is less than the low link value of the node your edge is going to.
        
        Time Complexity: O(V+E)
        Space Complexity: O(V+E)
        """
        
        # building the adjacency matrix
        neighbor = collections.defaultdict(list)
        for i, j in connections:     # since it is a unidirectional graph
            neighbor[i].append(j)
            neighbor[j].append(i)
        visited = [0 for _ in range(n)]      # visited array that keeps track if a node has been previously visited or not
        lowLink = [i for i in range(n)]         # an array containing all the low link 
        answer = []                             # an array containing all the critical connections in a network
        
        
        def dfs(current_rank, previous_vertex, current_vertex):
            visited[current_vertex] = 1                    # make node as visited
            lowLink[current_vertex] = current_rank         # assign it's low link value
            
            for node in neighbor[current_vertex]:         # traverse all the neighbors of a node
                if node == previous_vertex: continue       # do not go backwards
        # if a node is not visited then perform a depth first search on that node looking for the lowest low link value
        # in the strongly connected connection.
                if not visited[node]:
                    dfs(current_rank+1, current_vertex, node)
                lowLink[current_vertex] = min(lowLink[current_vertex], lowLink[node]) # lowest low link value in the cycle
                
                if lowLink[node] > current_rank:               # if a bridge is found
                    answer.append([current_vertex, node])      # append the critical connection to the answer array.
        
        dfs(0,-1,0)
        
        return answer           # returns the answer
             