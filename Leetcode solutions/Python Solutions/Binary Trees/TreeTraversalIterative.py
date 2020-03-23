"""
All different kinds of Tree Traversal implemented iteratively
"""


"""
PreOrder Traversal: Root, Left, Right

Algorithm:

1) Create an empty stack nodeStack and push root node to stack.
2) Do following while nodeStack is not empty.
    Pop an item from stack and print it.
    Push right child of popped item to stack
    Push left child of popped item to stack

Since all the node is being visited exactly once therefore the time complexity is O(n)

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root: return
        
        stack = [root]
        answer = []
        
        while stack:
            temp = stack.pop()
            answer.append(temp.val)
            
            if temp.right:
                stack.append(temp.right)
            
            if temp.left:
                stack.append(temp.left)
                
        return answer

"""
InOrder Traversal: Left, Root, Right


Since all the node is being visited exactly once therefore the time complexity is O(n)

Time Complexity: O(n)
Space Complexity: O(n)

"""










"""
PostOrder Traversal: Left, Right, Root


Since all the node is being visited exactly once therefore the time complexity is O(n)

Time Complexity: O(n)
Space Complexity: O(n)

"""



"""
LevelOrder Traversal using DPS and PreOrder

Algorithm:


Since all the node is being visited exactly once therefore the time complexity is O(n)

Algorithm:

mantain a queue and initially add root to it.

while queue is not null: perform the following steps:
    Take all elements from queue, add their values to res list.
    create list "nextbatch" of all children of nodes in queue
    reassign queue = nextbatch

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root: return []

        queue=[root]
        res= []
        
        while len(queue):
            nextbatch=[]
            res.append([node.val for node in queue if node is not None])
            for node in queue:
                if node:
                    if node.left:
                        nextbatch.append(node.left)
                    if node.right:
                        nextbatch.append(node.right)
            queue = nextbatch
        return res