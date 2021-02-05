/*
LeetCode Problem 42. Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/
Written by: Mostofa Adib Shakib
Language: C++
*/


class Solution {
    
public:
    int getMaximumIndex(vector<int> &height) {
        int maximum = INT_MIN;
        int index = -1;

        for (int i = 0; i < height.size(); i++) {
            if (height[i] > maximum) {
                maximum = height[i];
                index = i;
            }
        }

        return index;
    }
    
    int getMaximum(int a, int b) {
        if (a > b) {
            return a;
        }
        else if (b > a) {
            return b;
        }
        else {
            return a;
        }
    }
    
    int getPartialSum(int startIndex, int endIndex, vector<int> &height) {
        int maximumSeenSoFar = 0;
        int partialSum = 0;
            
        for (int i = startIndex; i <= endIndex; i++) {
            
            if (height[i] < maximumSeenSoFar) {
                partialSum += maximumSeenSoFar-height[i];
            }
            maximumSeenSoFar = getMaximum(maximumSeenSoFar, height[i]);
        }
        
        return partialSum;
    }
    
    int trap(vector<int>& height) {
        if (height.size() == 0) {
            return 0;
        }
        
        int maxHeightIndex =  getMaximumIndex(height);
        int amount = 0;

        amount += getPartialSum(0, maxHeightIndex, height);
        
        reverse(height.begin(),height.end());
        
        amount += getPartialSum(0, height.size() - maxHeightIndex -1, height);
        
        return amount;
    }
};