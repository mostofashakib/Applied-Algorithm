"""
LeetCode Problem: 438. Find All Anagrams in a String
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
Language: Python
Written by: Mostofa Adib Shakib

Counter(bag or multiset) is a subclass of defaultdictionary.
Counter won't add new keys unlike a dictionary when you query for missing keys. 

"""

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        pattern_counter = Counter(p)
        running_counter = Counter()
        len_p = len(p)
        result = []

        for i in range(len(s)):
            
            # If index  >= length of the pattern.
            # then decrement the count of the (i - len_p)th character to remove it from 
            # the current (sliding) window.
            if i >= len_p:
                running_counter[s[i - len_p]] -= 1

                if running_counter[s[i - len_p]] == 0:
                    del running_counter[s[i  - len_p]]
            
            # Default: just increment the count of the current character.
            running_counter[s[i]] += 1
            
            # At any time, if running_counter == pattern_counter then append the result.
            if running_counter == pattern_counter:
                result.append(i - len_p + 1)

        return result