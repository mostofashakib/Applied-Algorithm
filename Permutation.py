"""
46 Leetcode. Permutations
https://leetcode.com/problems/permutations/
"""


"""


"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def all_perms(elements):
            if len(elements) <= 1:
                yield elements
            else:
                for (index, first_elmt) in enumerate(elements):
                    other_elmts = elements[:index]+elements[index+1:]
                    for permutation in all_perms(other_elmts): 
                        yield [first_elmt] + permutation
                    
        return all_perms(nums)