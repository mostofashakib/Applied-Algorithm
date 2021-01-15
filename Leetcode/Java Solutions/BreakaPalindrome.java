/*
LeetCode Problem: 1328. Break a Palindrome
Link: https://leetcode.com/problems/break-a-palindrome/
Written by: Mostofa Adib Shakib
Language: Java
Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
    public String breakPalindrome(String palindrome) {
        if (palindrome.length() == 1) {
            return "";
        }
        
        int length = palindrome.length();
        int index = -1;
        
        for (int i = 0; i < length/2; i++) {
            if (palindrome.charAt(i) != 'a') {
                index = i;
                break;
            }
        }
        
        if (index == -1) {
            return palindrome.substring(0, length-1) + "b";
        }
        
        return palindrome.substring(0, index) + "a" + palindrome.substring(index+1, length);
    }
}