/*
LeetCode Problem: 383. Ransom Note
Link: https://leetcode.com/problems/ransom-note/
Language: JavaScript
Written by: Mostofa Adib Shakib
*/


// Solution 1: Char array
// Time Complexity: O(n^2)
// Space Complexity: O(n)

var canConstruct = function(ransomNote, magazine) {

    // generates an array of characters since strings are immutable in JavaScript

    var magazineArray = magazine.split("");
    var ransomNoteArray = ransomNote.split("");
    
    for (var i = 0; i < ransomNoteArray.length; i++){
        var char = ransomNoteArray[i];

        // checks if the character also exists in the magazine array
        // if the character exists then remove the character
        // if the character doesn't exist then return false 
        
        if(magazineArray.includes(char)){
            magazineArray[magazineArray.indexOf(char)] = "";
        }
        else{
            return false;
        }
    }

    // if the entire ransomNote array is traversed then return true

    return true;
};



// Solution 2: Hash Table more efficient for large data sets
// Time Complexity: O(n)
// Space Complexity: O(n)


var canConstruct = function(ransomNote, magazine) {
    var hashmap = {};

    // generating the frequency table
    
    for (var i = 0; i < magazine.length; i++){
        var char = magazine[i]
        
        if(char in hashmap){
            hashmap[char] += 1;
            
        }
        else{
            hashmap[char] = 1;
        }
    }

    // for each character in ransomNote check if the character is present
    // in the frequency table if the character is present and the frequency is greater 
    // than 0 then decrement the frequency by one. If the above condition is False
    // return False if the room completes successfully then we know that we can
    // make the ransomNote from the magazine hence return True
    
    for (var i = 0; i < ransomNote.length; i++){
        var char = ransomNote[i]
        
        if(char in hashmap && hashmap[char] > 0){
            hashmap[char] -= 1;
        }
        else{
            return false;
        }
    }

    // if the entire ransomNote array is traversed then return true

    return true;
};