"""
1051 Leetcode. Height Checker
https://leetcode.com/problems/height-checker/
"""

"""

We sort the array at the beginning and then run a loop which loops over every element in the array.
if the element in the index of the sorted temporary array is not equal to the element in the index of the array at the beginning then
increment the counter. Repeat the process till the loop ends and then return the counter.

"""

class Solution(object):
	def heightChecker(self, heights):
		"""
		:type heights: List[int]
		:rtype: int
		"""
		temp = sorted(heights)
		count = 0
		for i in range(len(temp)):
			if temp[i] != heights[i]:
				count += 1
		return count