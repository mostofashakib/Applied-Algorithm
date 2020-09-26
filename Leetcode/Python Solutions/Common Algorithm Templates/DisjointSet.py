"""
Language: Python
Written by: Mostofa Adib Shakib

Optimization Techniques:

1) Union by Rank: We always attach the smaller tree to the root of the larger tree. Since it is the depth of the tree that affects
the running time, the tree with the smaller depth gets added under the root of the deeper tree. The depth of the tree only increases
if the depth of both the tree are the same

2) Path compression: The idea is the each node visited on the way to a root node may as well be attached directly to the
 root node; they all share the same representative.
"""

class DisjointSet:
  def __init__(self):
    self.parent = {}
    self.rank = {}

  # Creates a set containing only a given element in it

  def makeSet(self, universe):
    for i in universe:
      self.parent[i] = i
      self.rank[i] = 0

  # Determines in which subset a particular element is in an returns
  # the representative of that particular set

  def find(self, k):
    if self.parent[k] != k:
      # path compression
      # recursively finds the parent once
      self.parent[k] = self.find(self.parent[k])

    return self.parent[k]

  # Merges two different subsets into a single subset and representative
  # of one set becomes the representative of other

  def union(self, x, y):
    # finds the parent of a node
    xRoot = self.find(x)
    yRoot = self.find(y)

    # returns if both the nodes share the same parent
    if xRoot == yRoot:
      return
    
    # make the tree with the least depth the child of the tree with higher depth

    if self.rank[xRoot] > self.rank[yRoot]:
      self.parent[yRoot] = xRoot
    elif self.rank[xRoot] < self.rank[yRoot]:
      self.parent[xRoot] = yRoot
    else:
      # When the nodes in both trees have the same depth 
      self.parent[xRoot] = yRoot
      self.rank[yRoot] += 1

# A utility function needed to print the disjointSet

def printSets(universe, ds):

	print([ds.find(i) for i in universe])


if __name__ == '__main__':

	# universe of items
	universe = [1, 2, 3, 4, 5]

	# initialize DisjointSet class
	ds = DisjointSet()

	# create singleton set for each element of universe
	ds.makeSet(universe)
	printSets(universe, ds)

	ds.union(4, 3)  # 4 and 3 are in same set
	printSets(universe, ds)

	ds.union(2, 1)  # 1 and 2 are in same set
	printSets(universe, ds)

	ds.union(1, 3)  # 1, 2, 3, 4 are in same set
	printSets(universe, ds)
  