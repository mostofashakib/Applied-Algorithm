"""
Different variations of the Lowest common ancestor problem
"""

# We traverse from the bottom, and once we reach a node which matches one of the two nodes, we pass it up to its parent.
# The parent would then test its left and right subtree if each contain one of the two nodes.
# If yes, then the parent must be the LCA and we pass its parent up to the root.
# If not, we pass the lower node which contains either one of the two nodes (if the left or right subtree contains either p or q), or NULL (if both the left and right subtree does not contain either p or q) up.
# O(n)

def lca(root, a, b):
    if not root: return None
    if root.value == a or root.value == b: return root
    left = lca(root.left, a, b)
    right = lca(root.right, a, b)
    if left and right: 
        # a & b are on both sides
        return root
    else: 
        # EITHER a/b is on one side 
        # OR a/b is not in L&R subtrees
        return left if left else right

# With parent pointer
# find the height h(a), h(b)
# move the deeper node b up by h(a)-h(b) steps
# move a and b up together until a=b
# Time Complexity: O(h)   h = height
# Space Complexity: O(n)

def lca_parent(root, node_a, node_b):
    h_a = find_height(root, node_a)
    h_b = find_height(root, node_b)
    if h_b > h_a:
        node_a, node_b = node_b, node_a
        h_a,h_b = h_b,h_a
    for _ in range(h_b - h_a):
        node_b = node_b.parent
    while node_a != node_b:
        node_a = node_a.parent
        node_b = node_b.parent
    return node_a

def find_height(root, node):
    h = 0
    while node:
        node = node.parent
        h += 1
    return h


"""
Binary Search Tree Properties:

Left subtree of a node N contains nodes whose values are lesser than or equal to node N's value.
Right subtree of a node N contains nodes whose values are greater than node N's value.
Both left and right subtrees are also BSTs.

Algorithm:
1) Start traversing the tree from the root node.
2) If both the nodes p and q are in the right subtree, then move root to the right subtree.
3) If both the nodes p and q are in the left subtree, then move root to the left subtree.
4) If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees. and hence we return this common node as the LCA.

Time Complexity: O(n)
Space Complexity: O(1)

"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
