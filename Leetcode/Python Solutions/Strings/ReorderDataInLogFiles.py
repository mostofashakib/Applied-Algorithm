"""
LeetCode Problem 937. Reorder Data in Log Files

Link: https://leetcode.com/problems/reorder-data-in-log-files/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(NlogN)
Space complexity: O(N)
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        onlyDigits = []
        onlyAlphas = []
        
        # If the last character is a digit then we append the log to the onlyDigits array
        # else we append the log to the onlyAlphas array
        
        for log in logs:
            if log[-1].isdigit():
                onlyDigits.append(log)
            else:
                onlyAlphas.append(log)
        
        # Sort the onlyAlphas array by suffixes where suffixes is everything in a string after the indentifier
        sortedArrayAlphas = sorted(onlyAlphas, key = lambda x: x.split(' ')[1:])
        
        for index in range(1, len(sortedArrayAlphas)):
            # swap based on identifier since there is a tie between the suffixes 
            if sortedArrayAlphas[index-1].split(' ')[1:] == sortedArrayAlphas[index].split(' ')[1:]:
                if sortedArrayAlphas[index-1][:1] > sortedArrayAlphas[index][:1]:
                    temp = ''.join(sortedArrayAlphas[index])
                    sortedArrayAlphas[index] = ''.join(sortedArrayAlphas[index-1])
                    sortedArrayAlphas[index-1] = temp
                    
            
        return sortedArrayAlphas + onlyDigits