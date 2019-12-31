"""
All different kinds of Tree Traversal implemented recursively
"""


"""
PreOrder Traversal: Root, Left, Right

Algorithm:
1) Keep a global array to keep the answer and call the helper function
2) In the helper function if the root is emply then return
3) Append the value of the current node to the answer array.
4) In the helper function if the root is not empty then recurse to the left
5) In the helper function if the root is not empty then recurse to the right
6) Return the answer at the end

Since all the node is being visited exactly once therefore the time complexity is O(n)

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution(object):    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        
        def helper(root):
            if not root: return 
            answer.append(root.val)
            helper(root.left)
            helper(root.right)
            return answer
        
        return helper(root)



"""
InOrder Traversal: Left, Root, Right

Algorithm:
1) Keep a global array to keep the answer and call the helper function
2) In the helper function if the root is emply then return
3) In the helper function if the root is not empty then recurse to the left
4) Append the value of the current node to the answer array.
5) In the helper function if the root is not empty then recurse to the right
6) Return the answer at the end

Since all the node is being visited exactly once therefore the time complexity is O(n)

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        answer = []
        
        def helper(root):
            if not root: return
            
            helper(root.left)
            answer.append(root.val)
            helper(root.right)
            return answer
        
        return helper(root)


"""
PostOrder Traversal: Left, Right, Root

Algorithm:
1) Keep a global array to keep the answer and call the helper function
2) In the helper function if the root is emply then return
3) In the helper function if the root is not empty then recurse to the left
4) In the helper function if the root is not empty then recurse to the right
5) Append the value of the current node to the answer array.
6) Return the answer at the end

Since all the node is being visited exactly once therefore the time complexity is O(n)

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        answer = []
        
        def helper(root):
            if not root: return
            helper(root.left)
            helper(root.right)
            answer.append(root.val)
            return answer
        
        return helper(root)

"""
LevelOrder Traversal using DPS and PreOrder

Algorithm:

Ensure that the tree is not empty, and then call recursively the function helper(node, level), which takes the current node and its level as the arguments.

The helper function does the following :
    1) The output list here is called levels, and hence the current level is just a length of this list len(levels).
    2) Compare the number of a current level len(levels) with a node level. If you're still on the previous level - add the new one by adding a new list into levels.
    3) Append the node value to the last list in levels
    4) Process recursively child nodes if they are not None : helper(node.left / node.right, level + 1).

Since all the node is being visited exactly once therefore the time complexity is O(n)

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)

        return levels