/*
LeetCode Problem: 1151. Minimum Swaps to Group All 1's Together
Link: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/
Language: C++
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
*/

class Solution {
public:
    int sumOfAnArray(vector<int> &array) {
        int arraySum = 0;
        
        for (int i = 0; i < array.size(); i++) {
            arraySum += array[i];
        }
        
        return arraySum;
    }
    
    int minSwaps(vector<int>& data) {
        int length = data.size();
        int runningCount = data[0];
        int left = 0;
        int right = 1;
        int ans = 0;
        int countOnes = sumOfAnArray(data);
        
        while (right < length) {
            runningCount += data[right];
            
            if (right - left == countOnes) {
                runningCount -= data[left];
                left++;
            }
            
            ans = max(ans, runningCount);
            right++;
        }
        
        return countOnes - ans;
    }
};