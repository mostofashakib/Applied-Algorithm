/*
LeetCode Problem: 836. Rectangle Overlap
Link: https://leetcode.com/problems/rectangle-overlap/
Language: C++
Written by: Mostofa Adib Shakib

Time Complexity: O(1)
Space Complexity: O(1)
*/

class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        int rect1_x1 = rec1[0];
        int rect1_y1 = rec1[1];
        int rect1_x2 = rec1[2];
        int rect1_y2 = rec1[3];
        
        int rect2_x1 = rec2[0];
        int rect2_y1 = rec2[1];
        int rect2_x2 = rec2[2];
        int rect2_y2 = rec2[3];
        
        if ( rect1_y1 == rect1_y2 || rect1_x1 == rect1_x2 || rect2_x1 == rect2_x2 || rect2_y1 == rect2_y2)  {
            return false;
        }
        
        if ( (rect1_x1 < rect2_x2 && rect1_y1 < rect2_y2) && (rect2_x1 < rect1_x2 && rect2_y1 < rect1_y2) ) {
            return true;
        }
        
        return false;
    }
};