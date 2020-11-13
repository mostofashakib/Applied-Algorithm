"""
LeetCode Problem: 1209. Remove All Adjacent Duplicates in String II
Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Compplexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # Memoization
        @lru_cache(maxsize=None)
        def recursiveHelper(string):
            # count starts with 1 because if the previous char is uncounted
            count = 1
            
            for j in range(1, len(string)):
                # if the current char is the same as the previous one increment count by 1
                if string[j-1] == string[j]:
                    count += 1
                
                # if the current char is not the same as the previous one reset count
                elif string[j-1] != string[j]:
                    count = 1
                
                # if count is equal to k then recurse without the k adjacent chars
                if count == k:
                    return recursiveHelper(string[:j-k+1] + string[j+1:])
            
            # return the string which doesn't contain any equal adjacent k chars
            return string
        
        return recursiveHelper(s)   # call the recursive function