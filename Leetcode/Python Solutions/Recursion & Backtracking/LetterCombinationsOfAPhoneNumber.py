"""
LeetCode Problem: 17. Letter Combinations of a Phone Number
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n4^n)
Space Complexity: O(n)
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        mapping = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        def recursive_helper(index):
            if index == len(digits):
                result.append(''.join(current_string))
            else:
                # try all possible combinations
                for c in mapping[int(digits[index])]:
                    current_string[index] = c
                    # recursively call the next digit
                    recursive_helper(index+1)
        
        result = []
        current_string = [0] * len(digits)
        recursive_helper(0)
        return result