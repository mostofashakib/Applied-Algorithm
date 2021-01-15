/*
LeetCode Problem: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Written by: Mostofa Adib Shakib
Language: Java
*/

class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> hashmap = new HashMap<Character, Character>();
        hashmap.put('(',')');
        hashmap.put('[', ']');
        hashmap.put('{', '}');
        
        Stack<Character> stack = new Stack<Character>();   
        int length = s.length();
        
        for (int i = 0; i < length; i++) {
            
            if ( s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{' ) {
                stack.push(s.charAt(i));
            }
            
            else {
                
                if ( stack.size() > 0 && hashmap.get(stack.peek()) == s.charAt(i) ) {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
        }
        return stack.size() == 0 ? true:false; 
    }
}