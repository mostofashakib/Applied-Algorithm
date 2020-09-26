""" Kruskal's Minimum spanning tree

Language: Python
Written by: Mostofa Adib Shakib

Reading Material: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
                  https://www.ics.uci.edu/~eppstein/161/960206.html

Time Complexity: O(E log E)

Optimization Techniques:

1) Union by Rank: We always attach the smaller tree to the root of the larger tree. Since it is the depth of the tree that affects
the running time, the tree with the smaller depth gets added under the root of the deeper tree. The depth of the tree only increases
if the depth of both the tree are the same

2) Path compression: The idea is the each node visited on the way to a root node may as well be attached directly to the
 root node; they all share the same representative.
"""


class DisjointSet:
  def __init__(self, vertices):
    self.vertices = vertices
    self.parent = {}
    self.rank = {}
    self.graph = []

  def makeSet(self, universe):
    for i in universe:
      self.parent[i] = i
      self.rank[i] = 0
  
  def addEdge(self, u, v, weight):
    self.graph.append([u, v, weight])

  def find(self, k):
    if self.parent[k] != k:
      # path compression
      # recursively finds the parent once
      self.parent[k] = self.find(self.parent[k])

    return self.parent[k]

  def union(self, x, y):
    # finds the parent of a node
    xRoot = self.find(x)
    yRoot = self.find(y)

    if xRoot == yRoot:
      return
    
    # make the tree with the least depth the child of the tree with higher depth
    if self.rank[xRoot] > self.rank[yRoot]:
      self.parent[yRoot] = xRoot
    elif self.rank[xRoot] < self.rank[yRoot]:
      self.parent[xRoot] = yRoot
    else:
      # find they both have the same depth 
      self.parent[xRoot] = yRoot
      self.rank[yRoot] += 1

  def KruskalMST(self):
    i = 0 # An index variable, used for sorted edges 
    e = 0 # An index variable, used for result[] 
    result = [] # #This will store the resultant MST

    # Sort all the edges in non-decreasing order of their weight
    sortedArray = sorted(self.graph, key = lambda item: item[2])

    # Number of edges to be taken is equal to V-1
    while e != self.vertices-1:
      # Pick the smallest edge and increment the index for next iteration 
      u, v, w = sortedArray[i]
      i += 1

      xRoot = self.find(u)
      yRoot = self.find(v)

      # If including this edge does't cause cycle, include it in result and increment the index of result for next edge

      if xRoot != yRoot:
        e += 1
        self.union(xRoot, yRoot)
        result.append([u, v, w])

    print ("Following are the edges in the constructed MST")
    for u,v,weight  in result: 
        print ("%d -- %d == %d" % (u,v,weight)) 


def printSets(universe, ds):

	print([ds.find(i) for i in universe])


if __name__ == '__main__':

	# universe of items
  universe = [0, 1, 2, 3]

  # initialize DisjointSet class
  ds = DisjointSet(4)

  # create singleton set for each element of universe
  ds.makeSet(universe)
  printSets(universe, ds)

  ds.addEdge(0, 1, 10)
  ds.addEdge(0, 2, 6)
  ds.addEdge(0, 3, 5) 
  ds.addEdge(1, 3, 15) 
  ds.addEdge(2, 3, 4)
  ds.KruskalMST()