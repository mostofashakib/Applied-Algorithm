"""
LeetCode Problem: 1086. High Five
Link: https://leetcode.com/problems/high-five//
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashmap = {}  # declaring the hashmap data structure 
        
        # populating the hashmap
        
        for i in items:
            id_number = i[0]  # the student's id number
            score = i[1]      # the student's score
            
            if id_number not in hashmap:
                hashmap[id_number] = [score]
            else:
                hashmap[id_number].append(score)
                
        result = []
        
        # traverse the items in the hashmap
        
        for key, value in hashmap.items():
            
            # if the array contains more than 5 scores
            # sort the array first in descending order and then pick the top 5 scores
            
            if len(value) > 5:
                value = sorted(value, reverse = True)
                total = sum(value[:5])
                average =  total//5
                result.append([key, average])
            else:                
                average = sum(value)//len(value)
                result.append([key, average])
            
        return result