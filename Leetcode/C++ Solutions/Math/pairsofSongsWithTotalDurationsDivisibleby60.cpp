/*
LeetCode Problem: 1010. Pairs of Songs With Total Durations Divisible by 60
Link: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
Language: C++
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        vector<int> array = {};
        vector<int> specialCases = {0, 30};
        int count = 0;
        
        for (int i = 0; i <= 60; i++) {
            array.push_back(0);
        }
        
        for (auto it : time) {
            array[it % 60]++;
        }
        
        for (int i = 1; i < 30; i++) {
            count += (array[i] * array[60-i]);
        }
        
        for (auto it : specialCases) {
            count += ( (array[it] - 1) * (array[it])/2 );
        }
        
        return count;
    }
};