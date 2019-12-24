"""
LeetCode Problem: 12. Integer to Roman
Link: https://leetcode.com/problems/integer-to-roman/
Written by: Mostofa Adib Shakib
Language: Python


"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        res = ''                   # builds up the resulting string
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
        i = 0
        while num > 0:
            if num - values[i] >= 0:    # greedily takes the highest number out.
                res += numerals[i]
                num -= values[i]
            else:
                i += 1

        return res