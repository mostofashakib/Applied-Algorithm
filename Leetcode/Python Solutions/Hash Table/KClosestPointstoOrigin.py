"""
LeetCode Problem: 973. K Closest Points to Origin
Link: https://leetcode.com/problems/k-closest-points-to-origin/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

# Fastest solution

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def squaredNumber(x):
            return ( (x[0])**2 + (x[1])**2 )**(0.5)
        
        points = sorted(points, key = squaredNumber)
                    
        return points[:K]

# Second solution

from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def squaredNumber(x,y):
            return ( (x)**2 + (y)**2 )**(0.5)
        
        hashmap = defaultdict(list)
        
        for i in points:
            distance = squaredNumber(i[0], i[1])
            if distance not in hashmap:
                hashmap[distance] = [i]
            else:
                hashmap[distance].append(i)
        
        hashmap = sorted(hashmap.items(), key = operator.itemgetter(0))
        
        ans = []
        
        for i in hashmap:
            j = 0
            if K > 0 and len(i[1]) > 0:
                while j < len(i[1]):
                    ans.append(i[1][j])
                    j += 1
                    K -= 1
                    
        return ans