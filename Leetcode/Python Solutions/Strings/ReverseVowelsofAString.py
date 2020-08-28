"""
LeetCode Problem: 345. Reverse Vowels of a String
Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        length = len(s)        # Calculates the length of the string
        vowels = "aeiouAEIOU"  # A string that contains all the lower-cased and upper-cased vowels
        indexArray = []        # An array that stores the index of all the vowels in the input string
        
        # index is your current position in the string
        # The for loop traverses from the 0th position to the end of the string
        
        for index in range(length):
            character = s[index] 
            if character in vowels:
                                          # This line only executes if the character is a vowel
                indexArray.append(index)  # This appends the index of the vowel into the array
        
        # In order to swap characters we need to convert the string to an array
        
        s = list(s)                       # converts a string to an array
        
        # Remember that the index array contains the position of all the vowels
        # If there are atmost one vowel then we do not need to do anything
        # This while loop only executes if the length of the array is greater than one
        
        
        while len(indexArray) > 1:
            # This removes the first element from the indexArray array and assigns it to the variable startingPosition
            startingPosition = indexArray.pop(0)
            # This removes the last element from the indexArray array and assigns it to the variable endingPosition
            endingPosition = indexArray.pop()
            
            # This swaps the position of the two characters in the array s
            s[startingPosition], s[endingPosition] = s[endingPosition], s[startingPosition]
        
        return ''.join(s)               # This converts a string to an array