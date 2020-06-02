"""
LeetCode Problem: 953. Verifying an Alien Dictionary
Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(C), where C is the total content of words.
Space Complexity: O(1)
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def helper(word1, word2):
            i = 0
            compare_val = 0
            
            
            # Find the first difference word1[i] != word2[i] and check their position in the sequence
            while i < len(word1) and i < len(word2) and compare_val == 0:
                compare_val = hashmap[word1[i]] - hashmap[word2[i]]
                i += 1
            
            # If we didn't find a first difference, the words are like ("app", "apple")
            if compare_val == 0:
                compare_val = len(word1) - len(word2)
                
            return compare_val
            
        hashmap = {}
        
        # map the alien language to our language
        
        for i in range(len(order)):
            hashmap[order[i]] = i
            
        for i in range(1, len(words)):
            if helper(words[i-1], words[i]) > 0:
                return False
                
        return True