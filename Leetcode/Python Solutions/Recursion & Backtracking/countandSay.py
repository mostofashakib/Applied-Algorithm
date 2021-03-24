"""
LeetCode Problem: 38. Count and Say
Link: https://leetcode.com/problems/count-and-say/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(2^N)
Space Complexity: O(2^N)
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        s = self.countAndSay(n-1)

        result = ""
        count = 1
        i = 1
        
        while i < len(s) + 1:
            if i < len(s) and s[i] == s[i-1]:
                count += 1
            else:
                result += str(count) + s[i-1]
                count = 1
            i += 1
            
        return result