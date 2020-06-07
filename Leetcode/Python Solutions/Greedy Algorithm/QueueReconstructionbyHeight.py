"""
LeetCode Problem: 406. Queue Reconstruction by Height
Link: https://leetcode.com/problems/queue-reconstruction-by-height/
Language: Python
Written by: Mostofa Adib Shakib

Algorithm:

1) Sort people:
    In the descending order by height.
    Among the guys of the same height, in the ascending order by k-values.

2) Take guys one by one, and place them in the output array at the indexes equal to their k-values.
3) Return output array.

Time complexity : O(n^2)
Space complexity : O(n).
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people , key = lambda x: (-x[0], x[1]))
        output = []
        
        for i in people:
            output.insert(i[1], i)
            
        return output
