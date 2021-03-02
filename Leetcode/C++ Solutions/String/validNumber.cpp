/*
LeetCode Problem: 65. Valid Number
Link: https://leetcode.com/problems/valid-number/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n)
Space Complexity: O(1)
*/

class Solution {
public:
    bool isNumber(string s) {
        int i = 0;
        int length = s.size();
        int count_point = 0;
        int count_num = 0;
        int count_e = 0;
        
        // Consume all the write spaces at the beginning of the string
        while( i < length && s[i]==' ') {
            i++;
        }
        
        // Consume the sign character if at the start of the string
        if ( i < length && (s[i]=='+' || s[i]=='-') ) {
            i++;
        }
        
        // Count all the deciamls and integer before the exponent character
        while ( i < length && ( (s[i] >= '0' && s[i] <= '9') || s[i]=='.') ) {
            s[i++]=='.' ? ++count_point : ++count_num;
        }
        
        // Return False if there is more than one decimal or if the integer count is 0
        if (count_point > 1 || count_num == 0) {
            return false;
        }
        
        // Consume the exponent if present in the given string
        if( i < length && s[i]=='e' || i < length && s[i]=='E') {
            i++;
            
            // Consume the sign character if present
            if( i < length && (s[i]=='+' || s[i]=='-') ) {
                i++;
            }
            
            // Count the number of integers present after the exponent
            while( i < length &&(s[i]>='0' && s[i]<='9') ) {
                i++;
                count_e++;
            }
            
            // Return false if the number of integers in the exponent part is 0
            if(count_e == 0) {
                return false;
            }
        }
        
        // Consume all the white spaces at the end of the string
        while ( i < length && s[i] == ' ') {
            i++;
        }
        
        // This will only return true if the string is a valid number with the given constraints
        return i == length;
    }
};