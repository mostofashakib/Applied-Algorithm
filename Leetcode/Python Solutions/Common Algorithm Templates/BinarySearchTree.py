"""
Language: Python
Written by: Mostofa Adib Shakib

****There must be no duplicate nodes.

Binary Search Tree, is a node-based binary tree data structure which has the following properties:
    The left subtree of a node contains only nodes with keys lesser than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.

"""

# Recursive Binary Search Tree

def binarySearchTreeRecursive(root, target): 
      
    # Base Cases: root is null or target is present at root 
    if root is None or root.val == target: 
        return root 
  
    # target is greater than root's target 
    if root.val < target: 
        return binarySearchTreeRecursive(root.right,target) 
    
    # target is smaller than root's target 
    return binarySearchTreeRecursive(root.left,target) 


# Iterative Binary Search Tree

def binarySearchTreeIterative(root, target): 
      
    # Traverse until root reaches to dead end  
    while root != None:

        if target == root.val:
            return True
          
        # pass right subtree as new tree  
        elif target > root.val:  
            root = root.right 
  
        # pass left subtree as new tree 
        else: 
            root = root.left

    return False