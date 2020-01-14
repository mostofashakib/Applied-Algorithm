"""
Leetcode 273. Integer to English Words
https://leetcode.com/problems/integer-to-english-words/
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        oneto19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'XX XX Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        # XX are just dummy variables which acts like place holders.
        
        if num == 0:
            return 'Zero'

        def Int2Words(n):           # the recursive function
            if n < 20:              # less than twenty.
                return oneto19[n-1:n]
            if n < 100:             # less than a hundred
                return [tens[n//10]] + Int2Words(n%10)
            if n <1000:             # less than a thousand
                return Int2Words(n//100) + ['Hundred'] + Int2Words(n%100)
            if n < 1000000:         # less than a million
                return Int2Words(n//1000) + ['Thousand'] + Int2Words(n%1000)
            if n < 1000000000:      # less than a billion
                return Int2Words(n//1000000) + ['Million'] + Int2Words(n%1000000)
            if n < 1000000000000:   # less than a trillion 
                return Int2Words(n//1000000000) + ['Billion'] + Int2Words(n%1000000000)

        return ' '.join(Int2Words(num))    # returns the answer