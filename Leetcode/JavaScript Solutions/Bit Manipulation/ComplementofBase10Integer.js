/*
LeetCode Problem 1009. Complement of Base 10 Integer
Link: https://leetcode.com/problems/complement-of-base-10-integer/
Written by: Mostofa Adib Shakib
Language: JavaScript

Time complexity: O(1)  Since the number of iterations is not more than 32.
Space complexity: O(1)
*/

var bitwiseComplement = function(N) {
    if (N == 0){
        return 1;
    };
    
    var mask = 1;
    var countLeft = N;
    
    while(countLeft){
        
        // flip the bits
        N = N ^ mask
        
        // preparing batch for the next shift
        mask = mask << 1
        countLeft = countLeft >> 1
    }
    return N;
};