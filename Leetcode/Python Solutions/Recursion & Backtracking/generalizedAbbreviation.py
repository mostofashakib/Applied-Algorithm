"""
LeetCode Problem: 320. Generalized Abbreviation
Link: https://leetcode.com/problems/generalized-abbreviation/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n^2n)
Space Complexity: O(n)
"""

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        if not word:
            return [""]
        
        length = len(word)
        result = []
        
        def backtrack(idx, path):
            if idx == length:
                result.append(''.join(path))
                return
            else:
                for i in range(idx, length):
                    if not path or path[-1].isdigit():
                        path.append(word[idx:i+1])
                        backtrack(i+1, path)
                        path.pop()
                    if not path or path[-1].isalpha():
                        path.append(str(len(word[idx:i+1])))
                        backtrack(i+1, path)
                        path.pop()
                        
        backtrack(0, [])
        return result