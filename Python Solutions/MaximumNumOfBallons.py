"""
1189 Leetcode. Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/
"""


"""

For every character(key) in word, it will find the total number of occurance of that with in the text and also the word itself
and then calculate their ratio text.count(ch) // word.count(ch).
so,
for word = 'balloon' and text = 'nlaebolko'

text.count('b') // word.count('b') = 1 // 1 = 1
text.count('a') // word.count('a') = 1 // 1 = 1
text.count('l') // word.count('l') = 2 // 2 = 1
text.count('l') // word.count('l') = 2 // 2 = 1
text.count('o') // word.count('o') = 2 // 2 = 1
text.count('o') // word.count('o') = 2 // 2 = 1
text.count('n') // word.count('n') = 1 // 1 = 1

Then we calculate the minimum of all the above calculated values.

"""

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        word = 'balloon'
        return min(text.count(key)//word.count(key) for key in word)