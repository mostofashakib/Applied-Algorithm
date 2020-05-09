/*
LeetCode Problem 387. First Unique Character in a String
Link: https://leetcode.com/problems/first-unique-character-in-a-string/
Written by: Mostofa Adib Shakib
Language: JavaScript

Time Complexity: O(n)
Space Complexity: O(n)
*/

/**
 * @param {string} s
 * @return {number}
 */
 
var firstUniqChar = function(s) {
    hashmap = {};
    charArray = s.split('');
    
    // generating a hashtable with it's index and frequency.

    for(var i = 0; i < charArray.length; i++){
        if(charArray[i] in hashmap){
            hashmap[charArray[i]][0] += 1;
        } else{
            hashmap[charArray[i]] = [1, i];
        }
    }
    
    // returns the index of the first element whose frequency is 1.

    for(var i = 0; i < charArray.length; i++){
        if(hashmap[charArray[i]][0] == 1){
            return hashmap[charArray[i]][1];
        }
    }

    return -1   // return -1 if none of the characters in the string are unique
};