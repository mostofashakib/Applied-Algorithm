/*
LeetCode Problem 128. Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Written by: Mostofa Adib Shakib
Language: C++
*/

class Solution {
public:
    
    int getMaximum(int x, int y) {
        return (x > y) ? x:y;
    }
    
    int longestConsecutive(vector<int>& nums) {
        unordered_set <int> hashSet;
        unordered_set <int> visited;
        int length = nums.size();
        int ans = 0;
        
        for (int i = 0; i < length; i++) {
            hashSet.insert(nums[i]);
        }
        
        for (int i = 0; i < length; i++) {
            int streak = 1;
            int currentLeft = nums[i];
            int currentRight = nums[i];
            
            while ( hashSet.find(currentLeft-1) != hashSet.end() && visited.find(currentLeft-1) == visited.end()) {
                visited.insert(currentLeft-1);
                streak++;
                currentLeft -= 1;
            }
            
            while ( hashSet.find(currentRight+1) != hashSet.end() && visited.find(currentRight+1) == visited.end()) {
                visited.insert(currentRight+1);
                streak++;
                currentRight += 1;
            }
            
            ans = getMaximum(ans, streak);
        }
        
        return ans;
    }
};