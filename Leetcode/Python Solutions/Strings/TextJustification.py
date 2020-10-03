"""
LeetCode Problem: 68. Text Justification
Link: https://leetcode.com/problems/text-justification/
Written by: Mostofa Adib Shakib
Language: Python

n = length of the words array
m = length of each individual word

Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        n = len(words)
        result = []
        
        while i < n:
            j = i + 1
            lineLength = len(words[i])
            
            while (j < n) and (lineLength + len(words[j]) + j-i-1) < maxWidth:
                lineLength += len(words[j])
                j += 1
            
            wordCount = j-i
            totalSpaces = maxWidth - lineLength
            
            if wordCount == 1 or j >= n:
                result.append(self.leftJustify(words, totalSpaces, i, j))
                
            else:
                result.append(self.middleJustify(words, totalSpaces, i, j))
            
            i = j
        
        return result
                
    def leftJustify(self, words, totalSpaces, i, j):
        mandatorySpaces = j-i-1
        extraSpaces = totalSpaces - mandatorySpaces
        string = ""
        
        k = i
        
        while k < j:
            if mandatorySpaces > 0:
                string += words[k] + " "
                mandatorySpaces -= 1
            else:
                string += words[k] + " "*extraSpaces
            
            k += 1
            
        return string
    
    def middleJustify(self, words, totalSpaces, i, j):
        spaceNeeded = j-i-1
        spaceGaps = totalSpaces // (spaceNeeded)
        extraSpaces = totalSpaces % (spaceNeeded)
        string = words[i]
        k = i+1
        
        while k < j:
            if extraSpaces > 0:
                string += " "*(spaceGaps+1) + words[k]
                extraSpaces -= 1
            else:
                string += " "*spaceGaps + words[k]
            
            k += 1
            
        return string