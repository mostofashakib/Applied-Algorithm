"""
LeetCode Problem: 1592. Rearrange Spaces Between Words
Link: https://leetcode.com/problems/rearrange-spaces-between-words/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        
        wordDict = text.split()
        wordCount = len(wordDict)
        
        # Special case - when text only has one word
        
        if wordCount == 1:
            if n > 1 and text[0] == " ":
                return wordDict[0] + " "*(n-len(wordDict[0]))
            else:
                return text

        whiteSpaces = 0
        string = ""
        extraSpace = 0
        
        # Counts the total number of white spaces
        
        for i in text:
            if i == " ":
                whiteSpaces += 1
        
        extraSpace = whiteSpaces % (wordCount-1)
        spaceGaps = whiteSpaces//(wordCount-1)
        
        for i in range(wordCount):
            word = wordDict[i]
            if i != wordCount-1:
                string += word + " "*spaceGaps
            else:
                string += word
        
        if extraSpace > 0:
            string += " "*extraSpace
            
        return string