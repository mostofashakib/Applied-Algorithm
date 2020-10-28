"""
LeetCode Problem: 1268. Search Suggestions System
Link: https://leetcode.com/problems/search-suggestions-system/
Language: Python
Written by: Mostofa Adib Shakib

n = length of the searchWord
m = length of the products array

Time complexity: O(n*m)
Space Complexity: O(h)
"""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)  # This sorts the given input array lexicographically
        result = []                  # Sorts the results
        
        # Traverse the search word
        
        for i in range(len(searchWord)):
            sub_string = searchWord[:i+1]       # Create different substrings
            temp = []                           # Used to store intermediate results
            
            for word in products:
                if word.startswith(sub_string): # Checks if a given word starts with the current substring
                    temp.append(word)           # If a given word starts with the current substring then store it in temp
        
            result.append(temp[:3])             # This limits the product names to three
            
        return result                           # Returns the result