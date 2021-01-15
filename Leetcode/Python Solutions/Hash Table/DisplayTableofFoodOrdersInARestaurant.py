"""
LeetCode Problem: 1418. Display Table of Food Orders in a Restaurant
Link: https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
Written by: Mostofa Adib Shakib
Language: Python

M = Number of tables + 1
N = Number of rows + 1

Time Complexity: O (M*N)
Space Complexity: O (M*N)
"""

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        hashmap = {}
        possibleFood  = set()       # Keeps track of all the unique foods ordered
        visitedTable = set()        # Keeps track of all the tables served

        # If the tableNumber does not exist in the first hashmap then we initialize a second hashmap and map the tableNumber to the second hashmap.
        # For the individual table number the key is going to be the name of the food and the value is going to be how many times did we order
        # that specific food for that specific table.
        
        for subArray in orders:
            tableNumber = subArray[1]
            food = subArray[2]

            visitedTable.add(int(tableNumber))
            possibleFood.add(food)
            
            if tableNumber in hashmap:
                if food not in hashmap[tableNumber]:
                    hashmap[tableNumber][food] = 1
                else:
                    hashmap[tableNumber][food] += 1
            
            else:
                hashmap[tableNumber] = {
                    food: 1
                }
        
        lengthTable = len(visitedTable)
        lengthFood = len(possibleFood)

        # Create a 2-D matrix
        
        matrix = [ ["0" for i in range(lengthFood+1)] for j in range(lengthTable+1) ]
        
        possibleFood = sorted(list(possibleFood))       # Lexicographically sort
        visitedTable = sorted(list(visitedTable))       # Lexicographically sort
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                # Populate the first row of the matrix with all the possible food items
                if r == 0:
                    if c == 0:
                        matrix[r][c] = "Table"
                    else:
                        matrix[r][c] = possibleFood[c-1]
                elif c == 0:
                    # For the first cell of every row we write the table number being served
                    if c == 0:
                        matrix[r][c] = str(visitedTable[r-1])
                    
                    if r > 0:
                        rowNumber = visitedTable[r-1]       # Finds the table Number
                        
                        # Iterates over the individual hashmap
                        for key, value in hashmap[str(rowNumber)].items():
                            index = matrix[0].index(key)        # Finds the right food item from the first row of the matrix

                            matrix[r][index] = str(value)       # Sets the right count for the right food item                   
        
        return matrix