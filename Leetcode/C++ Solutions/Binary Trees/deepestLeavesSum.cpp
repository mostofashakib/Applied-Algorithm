/*
LeetCode Problem: 1302. Deepest Leaves Sum
Link: https://leetcode.com/problems/deepest-leaves-sum/
Language: C++
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        queue<TreeNode*> queue;
        queue.push(root);
        int ans = 0;
        int length;
        TreeNode* node;
        
        while (!queue.empty()) {
            ans = 0;
            length = queue.size();
            
            for (int i = 0; i < length; i++) {
                node = queue.front();
                queue.pop();
                ans += node->val;
                
                if (node->left != NULL) {
                    queue.push(node->left);
                }
                
                if (node->right != NULL) {
                    queue.push(node->right);
                }
            }
        }
        return ans;
    }
};