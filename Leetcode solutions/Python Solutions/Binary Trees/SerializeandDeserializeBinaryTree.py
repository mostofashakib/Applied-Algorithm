"""

LeetCode Problem: 297. Serialize and Deserialize Binary Tree
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serializeHelper(root, string):
            if not root: return 'None,'                              # if it's a leaf node
            
            leftSerialization = serializeHelper(root.left, string)   # serialize left child
            rightSerialization = serializeHelper(root.right, string) # serialize right child
            
            return str(root.val) + ',' + leftSerialization + rightSerialization   # append the result to a string
        
        return serializeHelper(root, '')     # return the helper method

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserializeHelper(node_strings):
            if not node_strings: return None                 # if the queue is empty return None
             
            node = node_strings.popleft()                    # pop off an element from the left side of the queue
            
            if node == 'None': return None                   # if the element is a leaf node
            
            newNode = TreeNode(node)                         # create a new TreeNode with the value of node
            newNode.left = deserializeHelper(node_strings)   # deserialize left child
            newNode.right = deserializeHelper(node_strings)  # deserialize right child
            
            return newNode                                   # return the newly created node
        
        if not data: return None                              # if the string is empty return None
        
        node_strings = collections.deque(data.split(','))     # push all the elements into a queue
        
        return deserializeHelper(node_strings)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
