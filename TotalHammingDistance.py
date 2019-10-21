"""

477 Leetcode. Total Hamming Distance
https://leetcode.com/problems/total-hamming-distance/

"""




"""

This program converts all the integers in the array to their 32bit binary representation then count the number of zeros in each tuple.
For each tuple we multiply the number of zeros with the difference of the length of the array and the number of zeros in that tuple then
we increment the count with each result. Repeat the process for every integer in the array and return the count at the end of the
program.

"""

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        b = zip(*map('{:032b}'.format, nums))
        res = 0
        for i in b:
            a = i.count("0")
            res += a*(n-a)
        return res
