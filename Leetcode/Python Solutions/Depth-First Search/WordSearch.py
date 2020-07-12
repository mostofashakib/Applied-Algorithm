"""
LeetCode Problem: 79. Word Search
Link: https://leetcode.com/problems/word-search/
Language: Python
Written by: Mostofa Adib Shakib

Number of rows = M
Number of columns = N

Average time complexity: O(M*N * dfs complexity)
Space Complexity: O(M*N)

Worst-case time complexity:

If the dfs traverses in a zigzag fashion. The traversal would be E -> E-> D->A -> S -> F->C->S->E->C->B->A .
In such a case, the dfs would cost O(MN) for the worst case. 

Worst-case time complexity: O(M^2 * N^2)
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, column, idx, board, word, visited):

        	# boundary conditions

            if row < 0 or column < 0 or row >= len(board) or column >= len(board[0]) or visited[row][column] == True or board[row][column] != word[idx]:
                return False
            
            # if the idx value is equal to the length of the word then we have found a possible path

            if idx == len(word) - 1:
                return True
            
            # mark the current cell as visited

            visited[row][column] = True

            # if any of the dfs calls return True then we have found the given word in the matrix
            
            if dfs(row-1, column, idx+1, board, word, visited) or dfs(row+1, column, idx+1, board, word, visited) or dfs(row, column+1, idx+1, board, word, visited) or dfs(row, column-1, idx+1, board, word, visited):
                return True
            
            # mark the expored cell as unvisited

            visited[row][column] = False

        row = len(board)
        column = len(board[0])
        
        # we maintain a visited matrix as we cannot go back to the previous step

        visited = [ [False for i in range(column)] for j in range(row) ]
        
        for i in range(row):
            for j in range(column):
                if board[i][j] == word[0] and dfs(i, j, 0, board, word, visited):
                        return True

        # return False if the given word is not present in the matrix   
                 
        return False