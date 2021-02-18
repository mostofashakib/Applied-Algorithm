"""
LeetCode Problem: 722. Remove Comments
Link: https://leetcode.com/problems/remove-comments/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(S)
Space Complexity: O(S)
"""

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        newline = []
        ans = []
        
        for line in source:
            i = 0
            
            if not in_block:
                newline = []
                
            while i < len(line):
                # start of in-block comment
                if line[i:i+2] == '/*' and not in_block:
                    in_block = True
                    i += 1
                
                # end of in-block comment
                elif line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i += 1
                
                # single line comment
                elif not in_block and line[i:i+2] == '//':
                    break
                
                elif not in_block:
                    newline.append(line[i])
                i += 1
                
            if newline and not in_block:
                ans.append("".join(newline))

        return ans