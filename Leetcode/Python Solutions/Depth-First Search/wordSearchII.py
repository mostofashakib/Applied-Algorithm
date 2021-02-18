"""
LeetCode Problem: 212. Word Search II
Link: https://leetcode.com/problems/word-search-ii/
Language: Python
Written by: Mostofa Adib Shakib

Number of rows = M
Number of columns = N
Number of words = W

Time complexity: O(M*N * W)
Space Complexity: O(n) where n is the size of the recursion stack
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        
        def dfs(r, c, idx, word):
            
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[idx]:
                return False
            
            if idx == len(word)-1:
                return True
            
            idx += 1
            
            temp = board[r][c]      # backtracking
            
            board[r][c] = '$'
            
            found = dfs(r, c+1, idx, word) or dfs(r, c-1, idx, word) or dfs(r+1, c, idx,word) or dfs(r-1, c, idx, word)
            
            board[r][c] = temp
            
            return found
        
        for word in words:
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c] == word[0]:
                        if dfs(r, c, 0, word):
                            result.add(word)

        return result