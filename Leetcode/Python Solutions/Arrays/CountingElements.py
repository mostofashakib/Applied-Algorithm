"""
LeetCode 30 day chellenge. Counting Elements
Link: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/
Language: Python
Written by: Mostofa Adib Shakib
"""


"""
Approach 1:
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def countElements(self, arr: List[int]) -> int:
        if not arr: return 0
        
        hashset = set()
        count = 0
        
        for i in arr:
            if i not in hashset:
                hashset.add(i)
        
        for i in arr:
            if i+1 in hashset:
                count += 1
                
        return count

"""
Approach 2:
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def countElements(self, arr: List[int]) -> int:
        if not arr: return 0
        
        arr = sorted(arr)
        hashmap = {}
        count = 0
    
        for i in arr:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        for i in range(1, len(arr)):
            temp = arr[i-1] + 1
            
            if temp in hashmap:
                hashmap[temp] =- 1
                count += 1
                
        return count