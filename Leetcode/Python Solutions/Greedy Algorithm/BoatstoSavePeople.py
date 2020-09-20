"""
LeetCode Problem 881. Boats to Save People
Link: https://leetcode.com/problems/boats-to-save-people/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if sum(people) <= limit: return 1
        if not people: return 0
        
        n = len(people)
        count = 0
        people = sorted(people)
        firstPointer = 0
        secondPointer = n-1
        
        # At most two people
        while firstPointer <= secondPointer:
            count += 1
            # Increment the first pointer only if both the people can be fit in one boat
            if people[firstPointer] + people[secondPointer] <= limit:
                firstPointer += 1
            secondPointer -= 1
            
        return count