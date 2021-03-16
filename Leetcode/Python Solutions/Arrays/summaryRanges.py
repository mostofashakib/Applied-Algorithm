"""
LeetCode Problem: 228. Summary Ranges
Link: https://leetcode.com/problems/summary-ranges/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]

        for num in nums:
            if num-1 not in nums:
                nextNum = num + 1
                
                while nextNum in nums:
                    nextNum += 1
                
                if num == nextNum-1:
                    ans.append(str(num))
                else:
                    ans.append(str(num)+"->" + str(nextNum-1))
        return ans