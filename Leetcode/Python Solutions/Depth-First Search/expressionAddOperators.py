"""
LeetCode Problem: 282. Expression Add Operators
Link: https://leetcode.com/problems/expression-add-operators/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(4^N)
Space Complexity: O(N)
"""

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        
        def dfs(string, idx, total, prevOp):
            if idx == len(num) and target == total:
                return result.append(string)
            
            for j in range(idx + 1, len(num) + 1):
                subString = num[idx:j]
                value = int(subString)
                
                if num[idx] == "0" and subString != "0":
                    continue
                    
                if not string:
                    dfs(subString, j, value, value)
                else:
                    dfs(string + "+" + subString, j, total + value, value)
                    dfs(string + "-" + subString, j, total - value, -value)
                    dfs(string + "*" + subString, j, total - prevOp + prevOp * value, prevOp * value)
        
        dfs("", 0, 0, 0)
        return result