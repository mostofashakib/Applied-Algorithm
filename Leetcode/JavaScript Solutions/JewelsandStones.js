/*
LeetCode Problem 771. Jewels and Stones
Link: https://leetcode.com/problems/jewels-and-stones/
Written by: Mostofa Adib Shakib
Language: JavaScript
*/


# Solution 1
# Time Complexity: O(n)
# Space Complexity: O(n)

var numJewelsInStones = function(J, S) {
    var hashmap = {};
    var count = 0;
    
    for (var i in J){
        if(!hashmap.hasOwnProperty(i)){
            hashmap[J[i]] = 1
        }
    }
    
    for (var i in S){
        if(hashmap.hasOwnProperty(S[i])){
            count++;
        }
    }
    return count;
};


# Solution 2
# Time Complexity: O(n^2)
# Space Complexity: O(n)

var numJewelsInStones = function(J, S) {
    const array = J.split("")
    var count = 0;
    
    for (var i in S){
        if(array.includes(S[i])){
            count++;
        }
    }
    return count;
};