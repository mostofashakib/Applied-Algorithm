"""
LeetCode Problem: 8. String to Integer (atoi)
Link: https://leetcode.com/problems/string-to-integer-atoi/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def myAtoi(self, string: str) -> int:
        # This gets rid of any white spaces
        string = string.strip()

        if len(string) == 0:
            return 0
        
        if len(string) == 1:
            if string.isnumeric():
                # if the string only contains numeric values
                return int(string)
            else:
                return 0

        counter = ""
        flag = 1
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        first_value = True

        def helper(char):
            if char == "+" or char == "-" or char.isnumeric():
                return True
            return False

        for i in string:
            
            if first_value and i == " ":
                continue
            elif first_value and helper(i):
                if i == "-":
                    flag = -1
                elif i == "+":
                    first_value = False
                else:
                    counter += i
                first_value = False
                
            elif first_value == True and flag == 1 and len(counter) == 0:
                return 0
            
            elif first_value == False and i.isnumeric() == False and len(counter) == 0:
                return 0
            
            elif first_value == False and i.isnumeric():
                counter += i
            else:
                break
                
        number = int(counter) * flag

        if number > INT_MAX:
            return INT_MAX
        elif number < INT_MIN:
            return INT_MIN

        return number
        