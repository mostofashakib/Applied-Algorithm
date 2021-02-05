/*
LeetCode Problem: 54. Spiral Matrix
Link: https://leetcode.com/problems/spiral-matrix/
Written by: Mostofa Adib Shakib
Language: C++

n is the total number of cells in the matrix

Time Complexity: O(n)
Space Complexity: O(n)
*/


class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.size() == 0) {
            return {};
        }
        
        int rows = matrix.size();
        int columns = matrix[0].size();
        bool rFlag = false;
        bool cFlag = false;
        int i = 0;
        int j = 0;
        int forwards = 0;
        int rights = 0;
        int index = matrix.size() * matrix[0].size();   // maximum number of traversals
        vector<int> result;
        
        
        while (index > 0) {
            if (rFlag == false && cFlag == false) {
                
                if (j == columns - 1) {
                    cFlag = true;
                    result.push_back(matrix[i][j]);
                    i++;                    // To avoid duplications
                    forwards++;             // We shrink the top bounds
                }
                else {
                    result.push_back(matrix[i][j]);
                    j++;
                }
            }
            
            else if (rFlag == false && cFlag == true) {
                
                if (i == rows - 1) {
                    rFlag = true;
                    result.push_back(matrix[i][j]);
                    j--;                    // To avoid duplications
                    columns--;              // We shrink the right bounds
                }
                else {
                    result.push_back(matrix[i][j]);
                    i++;
                }
            }
            
            else if (rFlag == true && cFlag == true) {
                
                if (j == rights) {
                    cFlag = false;
                    result.push_back(matrix[i][j]);
                    i--;                    // To avoid duplications
                    rows--;                 // We shrink the bottom bounds
                }
                else {
                    result.push_back(matrix[i][j]);
                    j--;
                }
            }
            
            else {
                
                if (i == forwards) {
                    rFlag = false;
                    result.push_back(matrix[i][j]);
                    j++;                    // To avoid duplications
                    rights++;               // We shrink the left bounds
                }
                else {
                    result.push_back(matrix[i][j]);
                    i--;
                }
            }
            
            index--;
        }
        
        return result;
    }
};