/*
LeetCode Problem: 1614. Maximum Nesting Depth of the Parentheses
Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
Language: C++
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
public:
    int maxDepth(string s) {
        if (s.length() == 0 || (s.length() == 1 && s[0] != '(' && s[0] != ')' )) {
            return 0;
        }
        
        int balance = 0;
        int maximum = 0;
        int length = s.length();
        
        for (int i = 0; i < length; i++) {
            char character = s[i];
            
            if (character == '(') {
                balance++;
                maximum = max(balance, maximum);
            }
            else if (character == ')') {
                balance--;
            }
        }
        return maximum;
    }
};