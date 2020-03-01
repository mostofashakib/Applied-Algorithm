"""

LeetCode Problem: 451. Sort Characters By Frequency
Link: https://leetcode.com/problems/sort-characters-by-frequency/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n log n)
Space Complexity: O(h)

"""

class Solution:
    def frequencySort(self, s: str) -> str:
        
        if not s: return s             # if the string is empty
        
        hashmap = {}                   # initializing the hashmap data structure.
        
        # Populating the HashMap data structure to keep track of the frequency of each character.

        for i in list(s):
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        # sort the HashMap in descending order (The most frequent character takes first position)

        hashmap = sorted(hashmap.items(), key = operator.itemgetter(1), reverse=True)
        
        # initializing an empty string

        string = ""
        
        # multiplying the character with the number of occurances.

        for i in hashmap:
            string +=  i[0] * i[1]
        
        return string