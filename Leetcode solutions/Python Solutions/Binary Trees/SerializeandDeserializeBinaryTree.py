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

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def serializeHelper(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = serializeHelper(root.left, string)
                string = serializeHelper(root.right, string)
            return string
        
        return serializeHelper(root, '')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def deserializeHelper(node_strings):
            if not node_strings: return None
            
            node_string = node_strings.popleft()
            
            if node_string == "None": return None
            
            newNode = TreeNode(node_string)
            newNode.left = deserializeHelper(node_strings)
            newNode.right = deserializeHelper(node_strings)
            
            return newNode
        
        if not data: return None
        
        node_strings = collections.deque(data.split(','))
        
        return deserializeHelper(node_strings)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
