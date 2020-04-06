""" 
Description: Maximum Width of a Binary tree without counting null pointers
Link: https://www.geeksforgeeks.org/maximum-width-of-a-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

"""

class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
	def getMaxWidth(root): 
    	maxWidth = 0
    	h = height(root) 
    	for i in range(1,h+1): 
        	width = getWidth(root, i) 
        	if (width > maxWidth): 
            	maxWidth = width 
    	return maxWidth 
  
	def getWidth(root,level): 
    	if root is None: 
        	return 0
    	if level == 1: 
        	return 1
    	elif level > 1: 
        	return (getWidth(root.left,level-1) + getWidth(root.right,level-1)) 
 
	def height(node): 
    	if node is None: 
        	return 0
    	else: 
        	lHeight = height(node.left) 
        	rHeight = height(node.right) 
        	return (lHeight+1) if (lHeight > rHeight) else (rHeight+1) 