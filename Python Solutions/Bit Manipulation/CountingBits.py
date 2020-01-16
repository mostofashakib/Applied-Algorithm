"""
LeetCode Problem: 338. Counting Bits
Link: https://leetcode.com/problems/counting-bits/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def intoBinary(number):
            binarynumber=""
            if (number!=0):
                while (number>=1):
                    if (number %2==0):
                        binarynumber=binarynumber+"0"
                        number=number/2
                    else:
                        binarynumber=binarynumber+"1"
                        number=(number-1)/2
            else:
                binarynumber="0"
            return "".join(reversed(binarynumber))
        
        if num == 0: return [0]
        if num == 1: return [0,1]
        
        array = []
        array.append(0)
        
        for i in range(1, num+1):
            temp = intoBinary(i)
            count = 0
            for j in str(temp):
                if j == '1':
                    count = count + 1
            array.append(count)
        return array