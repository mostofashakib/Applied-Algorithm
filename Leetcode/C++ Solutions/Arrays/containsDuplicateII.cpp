/*
LeetCode Problem 219. Contains Duplicate II
Link: https://leetcode.com/problems/contains-duplicate-ii/
Written by: Mostofa Adib Shakib
Language: C++

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        // Initializing a hashmap
        map<int, int> hashMap;
        int number;
        
        // Iterate over the array
        for (int index = 0; index < nums.size(); index++) {
            // accessing the number from the array
            int number = nums[index];
            
            // check to see if the number exists in the hashmap or not
            if ( hashMap.find(number) == hashMap.end() ) {
                hashMap.insert({number, index});
            }
            
            else {
                // if the number doesn't exist in the hashmap then check if the difference between two integers is at most k.
                if ( index - hashMap[number] <= k) {
                    return true;
                }
                // update the indicies
                else {
                    hashMap[number] = index;
                }
            }
            
        }
        return false;
    }
};