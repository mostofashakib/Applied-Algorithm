/*
LeetCode Problem: 1578. Minimum Deletion Cost to Avoid Repeating Letters
Link: https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
Written by: Mostofa Adib Shakib
Language: C++

Time Complexity: O(n^2)
Space Complexity: O(1)
*/

class Solution {
public:
    // A helper function that calculates the minimum delection cost of a contineous sequence
    int helper(int firstPointer, int secondPointer, vector<int>& cost) {
        int totalSum = 0;
        int maximumNumber = INT_MIN;
        
        for (int i = firstPointer; i < secondPointer; i++) {
            if (cost[i] > maximumNumber) {
                maximumNumber = cost[i];
            }
            
            totalSum += cost[i];
        }
        
        return totalSum - maximumNumber;
    }
    
    int minCost(string s, vector<int>& cost) {
        int length = s.length();
        int i = 0;
        int streak = 0;
        int ans = 0;
        
        while (i < length) {
            while ( i + streak + 1  < length && s[i+streak] == s[i+streak+1]) {
                streak++;
            }
            
            if (streak > 0) {
                ans = ans + helper(i, i + streak + 1, cost);
                i = i + streak + 1;
                streak = 0;
            }
            else {
                i++;
            }
        }
        return ans;
    }
};