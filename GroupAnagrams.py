"""
LeetCode Problem: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Written by: Mostofa Adib Shakib
Language: Python

"""

from collections import defaultdict   #imports a default dictionary

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        srt = []      #a sorted array of elements
        
        for i in strs:
            temp = sorted(i)
            srt.append(''.join(temp))
                
        hashmap= defaultdict(list)    #initializing default dictionary
        
        for i in range(len(srt)):              # a hashmap is used to store all the anagrams of a given word
            hashmap[srt[i]].append(strs[i])
            
        return hashmap.values()  #returns a list of all the anagrams