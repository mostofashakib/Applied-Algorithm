"""
LeetCode Problem: 654. Maximum Binary Tree
Link: https://leetcode.com/problems/maximum-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

Time Compplexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        
        rootValue = max(nums)
        root = TreeNode(rootValue)
        index = nums.index(rootValue)
                
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        
        return root