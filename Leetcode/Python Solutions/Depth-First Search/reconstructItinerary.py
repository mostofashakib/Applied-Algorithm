"""
LeetCode Problem: 332. Reconstruct Itinerary
Link: https://leetcode.com/problems/reconstruct-itinerary/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.hashMap = defaultdict(list)
        stack = []
        
        for ticket in tickets:
            origin = ticket[0]
            destination = ticket[1]
            
            self.hashMap[origin].append(destination)
        
        # sort the itinerary based on the lexical order
        for origin, itinerary in self.hashMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)
                
        self.result = []
        self.DFS('JFK')

        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        destinationList = self.hashMap[origin]
        
        while destinationList:
            #while we visit the edge, we trim it off from graph.
            nextDestination = destinationList.pop()
            self.DFS(nextDestination)
            
        self.result.append(origin)