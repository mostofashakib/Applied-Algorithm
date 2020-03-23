/*
LeetCode Problem 412. Fizz Buzz
Link: https://leetcode.com/problems/fizz-buzz/
Written by: Mostofa Adib Shakib
Language: JavaScript
*/

var fizzBuzz = function(n) {
    var result = new Array(n-1);
    for(var i = 1; i < n+1; i++){
        if(i%15 == 0){
            result[i-1] =  'FizzBuzz';
        }
        else if (i % 5 == 0){
            result[i-1] = 'Buzz';
        }
        else if (i % 3 == 0){
            result[i-1] ='Fizz';
        }
        else{
            result[i-1] = i.toString();
        }
    }
    return result
};