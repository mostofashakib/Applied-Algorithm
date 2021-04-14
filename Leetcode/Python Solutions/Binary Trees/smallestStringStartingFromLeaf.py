"""
LeetCode Problem: 988. Smallest String Starting From Leaf
Link: https://leetcode.com/problems/smallest-string-starting-from-leaf/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        # Initialize the initial string to a character that has higher ASCII value than the character 'z'
        self.resultString = '~'
        
        @lru_cache(maxsize=None)
        def helper(root, string):
            if not root:
                return
            
            string += chr( ord('a') + root.val)
            
            if not root.left and not root.right:
                self.resultString = min(self.resultString, string[::-1])
                return
            
            helper(root.left, string)
            helper(root.right, string)
        
    
        helper(root, "")
        return self.resultString