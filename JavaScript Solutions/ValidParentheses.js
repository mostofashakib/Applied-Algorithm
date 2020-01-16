/*
LeetCode Problem 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Written by: Mostofa Adib Shakib
Language: JavaScript
*/


// Manually creating the stack class.

class Stack {   
    constructor() 
    { 
        this.items = []; 
    }
    
    push(element)
    { 
        this.items.push(element); 
    } 
    
    pop() 
    { 
        return this.items.pop(); 
    }
    
    peek()
    { 
        return this.items[this.items.length - 1]; 
    }
    
    isEmpty()
    { 
        return this.items.length == 0; 
    } 
} 


var isValid = function(s) {
    var openBracket = ['(', '{', '['];
    var parenthesis = { '(':')', '{':'}', '[':']' };
    var stack = new Stack();                                           // initializing a stack
    
    if(s.length < 0){
        return true;                                                   // checks to see if the string is empty
    }
    
    for(var i = 0; i < s.length; i++){
        if (openBracket.includes(s[i])){
            stack.push(s[i]);
        }
        else if( !stack.isEmpty() && s[i] == parenthesis[stack.peek()]){
            stack.pop(s[i]);
        }
        else{
            return false
        }
    }
    return stack.isEmpty() == true;
};