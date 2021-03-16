"""
LeetCode Problem: 459. Repeated Substring Pattern
Link: https://leetcode.com/problems/repeated-substring-pattern/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N^2)
Space Complexity: O(N)

Explanation:

Repeated pattern string looks like PatternPattern, and the others like Pattern1Pattern2.

Let's double the input string:

    PatternPattern --> PatternPatternPatternPattern

    Pattern1Pattern2 --> Pattern1Pattern2Pattern1Pattern2

Now let's cut the first and the last characters in the doubled string:

    PatternPattern --> *atternPatternPatternPatter*

    Pattern1Pattern2 --> *attern1Pattern2Pattern1Pattern*

It's quite evident that if the new string contains the input string, the input string is a repeated pattern string.
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]