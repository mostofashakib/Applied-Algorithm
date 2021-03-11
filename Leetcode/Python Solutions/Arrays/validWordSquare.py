"""
LeetCode Problem 422. Valid Word Square
Link: https://leetcode.com/problems/valid-word-square/
Written by: Mostofa Adib Shakib
Language: Python
"""

# Efficient
# Time Complexity: O(n*m)
# Space Complexity: O(1)

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:            
        rows = len(words)
        
        for r in range(rows):
            for c in range(len(words[r])):
                if c >= len(words) or r >= len(words[c]) or words[r][c] != words[c][r]:
                    return False
                
        return True


# Brute Force
# Time Complexity: O(n*m)
# Space Complexity: O(1)

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        matrix = []
        columns = 0
        
        for x in words:
            columns = max(columns, len(x))
            matrix.append(list(x))
            
        rows = len(matrix)
        c = 0
        
        while c < columns:
            rowStrings = ''.join(matrix[c])
            columnStrings = ""
            
            for r in range(rows):
                try:
                    columnStrings += matrix[r][c]
                except:
                    break
                
            c += 1
            
            if rowStrings != columnStrings:
                return False
                        
        return True