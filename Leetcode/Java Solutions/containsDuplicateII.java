/*
LeetCode Problem 219. Contains Duplicate II
Link: https://leetcode.com/problems/contains-duplicate-ii/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        // Initializing a hashmap
        Map<Integer, Integer> hashMap  = new HashMap<>();
        int number;
        
        // Iterate over the array
        for (int index = 0;  index < nums.length; index++ ) {
            // accessing the number from the array
            number = nums[index];
            
            // check to see if the number exists in the hashmap or not
            if ( !hashMap.containsKey(number) ) {
                hashMap.put(number, index);
            }
            else {
                // if the number doesn't exist in the hashmap then check if the difference between two integers is at most k.
                if ( index - hashMap.get(number) <= k) {
                    return true;
                }
                // update the indicies
                else {
                    hashMap.put(number, index);
                }
            }
        }
        return false;
    }
}