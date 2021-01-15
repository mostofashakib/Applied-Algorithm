"""
LeetCode Problem: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Written by: Mostofa Adib Shakib
Language: Python
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrings = []      #a sorted array of elements
        
        for i in strs:
            temp = sorted(i)
            sortedStrings.append(''.join(temp))
                
        hashmap= {}    #initializing default dictionary
        
        for i in range(len(sortedStrings)):      # a hashmap is used to store all the anagrams of a given word
            sortedWord = sortedStrings[i]
            # checks to see if the sortedStrings is present in the hashmap or not
            if sortedWord not in hashmap:
                hashmap[sortedWord] = [strs[i]]
            else:
                hashmap[sortedWord].append(strs[i])
            
        return hashmap.values()  #returns a list of all the anagrams