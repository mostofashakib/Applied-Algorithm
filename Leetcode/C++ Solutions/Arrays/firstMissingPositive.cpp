/*
LeetCode Problem 41. First Missing Positive
Link: https://leetcode.com/problems/first-missing-positive/
Written by: Mostofa Adib Shakib
Language: C++
*/


class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int smallestPositive  = 1;
        sort(nums.begin(), nums.end());                                     // sort the array into ascending order
        nums.erase( unique( nums.begin(), nums.end() ) , nums.end() );      // remove duplicate elements from the array
        
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] <= 0) {
                continue;
            }

            else if ( nums[i] == smallestPositive ) {
                smallestPositive++;
            }

            else {
                break;
            }
        }
     return smallestPositive;   
    }
};