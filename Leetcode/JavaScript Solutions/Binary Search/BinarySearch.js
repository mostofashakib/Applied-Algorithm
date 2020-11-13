/*
LeetCode Problem: 704. Binary Search
Link: https://leetcode.com/problems/binary-search/
Language: JavaScript
Written by: Mostofa Adib Shakib
*/


var search = function(nums, target) {
    // The array has to be sorted in ascending order for binary search to work
    // Time Complexity: O(LogN)
    // Space Complexity: O(1)
        
    var low = 0;                        //  Index of the first element in the array
    var high = nums.length - 1;         //  Index of the last element in the array
    
    // Check to see if the target is present in the array
    
    while (low <= high ) {
        var mid = (low+high)//2;        // Get the middle index
        
        // Check if the array at the middle is equal to the target
        if (nums[mid] == target) {
            return mid;
        }
        // If the array at the middle is bigger than the target than discard the right side
        else if (nums[mid] > target) {
            high = mid -1;
        }
        // If the array at the middle is smaller than the target than discard the left side
        else {
            low = mid + 1;
        }
    }
    
    return -1;                          // Return -1 if the target is not present in the array
    
};