"""
LeetCode Problem: 819. Most Common Word.
Link: https://leetcode.com/problems/most-common-word/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''                    # All the possible punctuations
        paragraph = paragraph.lower()                                        # Converts the string to all lowercase characters
        for x in paragraph:
            if x in punctuations: 
                paragraph = paragraph.replace(x, " ")                        # removes all possible punctuations from a string
        array = paragraph.split(' ')                                         # converts the string to a char array
        hashmap = {}                                                         # a hashmap is initialized
        
        for i in array:                                                      # traverse the char array                                       
            if i == "":                                                      # skip if you see whitespace
                continue             
            elif i not in hashmap and i not in banned:                       # if a word is not previously added to the hashmap
                hashmap[i] = 1
            elif i in hashmap and i not in banned:
                hashmap[i] += 1                                              # increment the word count if the word already exists in the hashmap
        
        maximum = max(hashmap.values())                                      # finds the maximum occurance of a certain word
        
        for key, value in hashmap.items():
            if value == maximum: 
                return key                                                   # returns the word with the maximum number of occurance