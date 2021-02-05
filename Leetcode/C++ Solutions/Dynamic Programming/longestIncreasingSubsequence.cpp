/*
LeetCode Problem: 300. Longest Increasing Subsequence
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Written by: Mostofa Adib Shakib
Language: C++

Time Complexity: O(n^2)
Space Complexity: O(n)
*/

// Without built-in functions

class Solution {
public:
    
    // Helper function to get the maximum of two numbers
    int getMaximum(int x, int y) {
        return (x > y) ? x:y;
    }
    
    // Helper function to get the maximum from a given array
    int getMaximumFromArray(vector<int> &nums) {
        int maximum = INT_MIN;
        
        for ( auto it : nums) {
            if ( it > maximum) {
                maximum = it;
            }
        }
        return maximum;
    }
    
    // Driver function that uses dynamic programming to calculate the length of LIS
    int lengthOfLIS(vector<int>& nums) {
        int length = nums.size();
        vector<int> dp(length, 1);                          // Initializes DP table
        
        // First Pointer
        for (int i = 1; i < length; i++) {
            int j = 0;
            
            // Second Pointer
            while ( j < i) {
                // If we can extend a given sequence
                if ( nums[j] < nums[i] ) {
                    dp[i] = getMaximum(dp[i], dp[j]+1);
                }
                
                j++;
            }
        }
        
        return getMaximumFromArray(dp);
    }
};


// Using built-in functions


class Solution {
public:
    
    int lengthOfLIS(vector<int>& nums) {
        int length = nums.size();
        vector<int> dp(length, 1);
        
        for (int i = 1; i < length; i++) {
            int j = 0;
            
            while ( j < i) {
                if ( nums[j] < nums[i] ) {
                    dp[i] = max(dp[i], dp[j]+1);
                }
                
                j++;
            }
        }
        
        return *max_element(dp.begin(), dp.end());
    }
};