"""
LeetCode Problem: 383. Ransom Note
Link: https://leetcode.com/problems/ransom-note/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        
        #generating the frequency table
        
        for i in magazine:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        # for each character in ransomNote check if the character is present
        # in the frequency table if the character is present and the frequency is greater 
        # than 0 then decrement the frequency by one. If the above condition is False
        # return False if the room completes successfully then we know that we can
        # make the ransomNote from the magazine hence return True
         
        for i in ransomNote:
            if i in hashmap and hashmap[i] > 0:
                hashmap[i] -= 1
            else:
                return False
            
        return True
        