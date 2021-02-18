/*
LeetCode Problem: 111. Minimum Depth of Binary Tree
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
Language: C++
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
public:
    int dfsHelper(TreeNode* node) {
        if ( node == NULL) {
            return INT_MAX;
        }
        
        if ( node->left == NULL && node-> right == NULL ) {
            return 1;
        }
        return 1 + min(dfsHelper(node->left), dfsHelper(node->right));
    }
    
    int minDepth(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        
        return dfsHelper(root);
    }
};