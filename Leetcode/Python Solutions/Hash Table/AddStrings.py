"""
LeetCode Problem: 415. Add Strings
Link: https://leetcode.com/problems/add-strings/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        # edge cases
        
        if num1 == "0" and num2 == "0": return num1
        
        elif num1 == "0":
            return num2
        
        elif num2 == "0":
            return num1
        
        # mapping string to integer
        
        hashmap = {"0": 0, "1": 1, "2": 2, "3":3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9 }
        
        number1 = 0
        number2 = 0
        length1 = len(num1) - 1
        length2 = len(num2) - 1
        
        for i in num1:
            number1 += hashmap[i] * 10 ** length1
            length1 -= 1
            
        for j in num2:
            number2 += hashmap[j] * 10 ** length2
            length2 -= 1
            
        return str(number1 + number2)