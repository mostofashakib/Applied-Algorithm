"""
LeetCode Problem: 640. Solve the Equation
Link: https://leetcode.com/problems/solve-the-equation/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def solveEquation(self, equation: str) -> str:
        X_LHS = 0                                   # Keeps track of the number of Xs on the left-hand side
        X_RHS = 0                                   # Keeps track of the number of Xs on the right-hand side
        INT_LHS = 0                                 # Keeps track of the total integer literal on the left-hand side
        INT_RHS = 0                                 # Keeps track of the total integer literal on the right-hand side
        length = len(equation)
        index = 0                                   # Iterator initialization
        switch = False                              # Flag used to switch from the LHS to the RHS
        
        while index < length:
            char = equation[index]
            
            # Calculates the number of Xs and total integer literal on the left-hand side
            if switch == False:
                # This is used to calculate negative integer literals
                if char == "-":
                    amount = 0
                    pointer = 1

                    # This is used when the value of an integer is greater than 9

                    while index+pointer < length and equation[index+pointer].isdigit():
                        amount = amount * 10 + int(equation[index+pointer])
                        pointer += 1
                    
                    INT_LHS -= amount
                    index += pointer
                
                # This is used to calculate positive integer literals
                elif char.isdigit():
                    amount = int(equation[index])
                    pointer = 1
                    
                    # This is used when the value of an integer is greater than 9

                    while index+pointer < length and equation[index+pointer].isdigit():
                        amount = amount * 10 + int(equation[index+pointer])
                        pointer += 1
                    
                    INT_LHS += amount
                    index += pointer
                    
                elif char == "x":
                    
                    # A check is made to ensure the multipility of x
                    if index-1 >= 0 and equation[index-1].isdigit():
                        amount = ""
                        pointer = -1
                        flag = False

                        # This is done to get x with multiplicity greater than one

                        while index+pointer >= 0 and equation[index+pointer].isdigit():
                            amount += equation[index+pointer]
                            pointer -= 1
                        
                        # This check is made to see if the coefficient of x is negative or not
                        if index-pointer >= 0 and equation[index+pointer] == "-":
                            flag = True
                        
                        amount = int(amount[::-1])      # Converts the string amount to an integer
                                                
                        INT_LHS -= amount if flag == False else -amount 
                        index += 1
                        X_LHS += amount if flag == False else -amount
                                                                    
                    else:
                        flag = False
                        
                        # This check is made to see if the coefficient of x is negative or not
                        if index-1 >= 0 and equation[index-1] == "-":
                            flag = True
                            
                        X_LHS += 1 if flag == False else -1
                        index += 1
                
                elif char == "=":
                    switch = True
                    index += 1
                    
                else:
                    index += 1
            
            # Calculates the number of Xs and total integer literal on the right-hand side   
            else:
                # This is used to calculate negative integer literals
                if char == "-":
                    pointer = 1
                    amount = 0

                    # This is used when the value of an integer is greater than 9

                    while index+pointer < length and equation[index+pointer].isdigit():
                        amount = amount * 10 + int(equation[index+pointer])
                        pointer += 1
                    
                    INT_RHS -= amount
                    index += pointer
                
                # This is used to calculate positive integer literals

                elif char.isdigit():
                    amount = int(equation[index])
                    pointer = 1

                    # This is used when the value of an integer is greater than 9

                    while index+pointer < length and equation[index+pointer].isdigit():
                        amount = amount * 10 + int(equation[index+pointer])
                        pointer += 1
                    
                    INT_RHS += amount
                    index += pointer
                    
                elif char == "x":

                    # A check is made to ensure the multipility of x
                    if index-1 >= 0 and equation[index-1].isdigit():
                        amount = ""
                        pointer = -1
                        flag = False

                        # This is done to get x with multiplicity greater than one
                        while index+pointer >= 0 and equation[index+pointer].isdigit():
                            amount += equation[index+pointer]
                            pointer -= 1
                            
                        amount = int(amount[::-1])
                        
                        # This check is made to see if the coefficient of x is negative or not
                        if index-pointer >= 0 and equation[index+pointer] == "-":
                            flag = True
                                                                                    
                        INT_RHS -= amount if flag == False else -amount 
                        index += 1
                        X_RHS += amount if flag == False else -amount
                                                                    
                    else:                    
                        flag = False
                        
                        # This check is made to see if the coefficient of x is negative or not
                        if index-1 >= 0 and equation[index-1] == "-":
                            flag = True
                            
                        X_RHS += 1 if flag == False else -1
                        index += 1
                else:
                    index += 1
        
        x = X_LHS-X_RHS
        INT = INT_RHS - INT_LHS
        
        # when the difference between the number of X on LHS and RHS is 1
        if x == 1 or x == -1:
            if X_LHS > X_RHS:
                return "x=" + str(INT_RHS - INT_LHS)
            else:
                return "x=" + str(INT_LHS-INT_RHS)
        
        # when the difference between the number of X on LHS and RHS not 1 and not 0
        elif x != 0:
            return "x=" + str(INT//x)
        else:
            # when the difference between the number of X and INT on LHS and RHS are both 0
            if x == 0 and INT == 0:
                return "Infinite solutions"
            else:
                return "No solution"