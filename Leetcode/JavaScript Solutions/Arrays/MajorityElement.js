/*
LeetCode 169. Majority Element
Link: https://leetcode.com/problems/majority-element/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: (n)
Space Complexity: O(n)
*/

var majorityElement = function(nums) {
    hashmap = {};
    maximum = [0,0];
    
    for(var i in nums){
        if(nums[i] in hashmap){
            hashmap[nums[i] ] += 1;
        } else{
            hashmap[nums[i] ] = 1;
        }
    }
    
    for (var key in hashmap){
        if(hashmap[key] > maximum[1]){
            maximum = [key, hashmap[key]]
        }
    }
    return maximum[0]
};
