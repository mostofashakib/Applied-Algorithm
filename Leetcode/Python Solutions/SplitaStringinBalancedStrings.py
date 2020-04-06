"""
1221 Leetcode. Split a String in Balanced Strings
https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""

"""
This solution uses a flag to keep track of a complete substring containing equal number of L & R. We do this with the help of a flag variable.
The flag variable is incremented for every 'R' and decremented for every 'L'. Whenever the value of flag is 0 we increment count indicating that a
substring with equal number of L & R has been found. At the end of the loop we return count which has the number of substrings that can be made
from a given string.
"""

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
                
        count = 0
        flag  = 0
        
        for i in range(len(s)):
            if s[i] == 'L':
                flag -= 1
                
            if s[i] == 'R':
                flag += 1
                
            if flag == 0:
                count += 1
                
        return count