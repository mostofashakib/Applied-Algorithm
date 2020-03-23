/*
LeetCode Problem 167. Two Sum II - Input array is sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Written by: Mostofa Adib Shakib
Language: JavaScript
*/


var twoSum = function(nums, target) {
    let FirstPointer = 0;
    let LastPointer = nums.length - 1;
    let result = new Array(1);
    
    while (FirstPointer < LastPointer){
        if(nums[FirstPointer] + nums[LastPointer] == target){
            result[0] = FirstPointer+1;
            result[1] = LastPointer+1;
            break;
        }
        else if(nums[FirstPointer] + nums[LastPointer] > target){
            LastPointer -= 1;
        }
        else{
            FirstPointer += 1;
        }
    }
    
    return result
};