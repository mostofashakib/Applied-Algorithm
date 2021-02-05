/*
LeetCode Problem 75. Sort Colors
Link: https://leetcode.com/problems/sort-colors/
Written by: Mostofa Adib Shakib
Language: C++
*/

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int startIndex = 0;
        int endIndex = nums.size() - 1;
        int index = 0;
        
        while ( index <= endIndex ) {
            
            if ( nums[index] == 0 ) {
                nums[index] = nums[startIndex];
                nums[startIndex] = 0;
                startIndex++;
                index++;
            }
            
            else if ( nums[index] == 2 ) {
                nums[index] = nums[endIndex];
                nums[endIndex] = 2;
                endIndex--;
            }
            
            else {
                index++;
            }
        }
    }
};