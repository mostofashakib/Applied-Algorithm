"""
LeetCode Problem: 187. Repeated DNA Sequences
Link: https://leetcode.com/problems/repeated-dna-sequences/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        stringLength = len(s)       # calculates the length of the input string
        
        # if the length of the string is 10 or less then there are none repeated sequences in the DNA
        
        if stringLength <= 10:
            return []
        
        visited = set()             # keeps track of all the DNA sequences seen so far
        ans = set()                 # only contains unique results
        
        for i in range(stringLength-9):
            if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
                substring = s[i:i+10]   # gets every possible DNA sequences
                
                # if the current DNA sequence has already been seen before we add it to the answer
                # else we add the current DNA sequence to the visited set
                
                if substring in visited:
                    ans.add(substring)
                else:
                    visited.add(substring)
        
        return ans