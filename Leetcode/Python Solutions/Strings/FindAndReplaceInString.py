"""
LeetCode Problem: 833. Find And Replace in String
Link: https://leetcode.com/problems/find-and-replace-in-string/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        modified = list(S)
        
        for index, source, target in zip(indexes, sources, targets):
            if not S[index:].startswith(source):
                continue
            else:
                modified[index] = target
                for i in range(index+1, len(source) + index):
                    modified[i] = ""
                    
        return "".join(modified)