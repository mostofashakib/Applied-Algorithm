"""
LeetCode Problem: 350. Intersection of Two Arrays II
Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""

1)  Brute Force: Uses two arrays

    Time complexity: O(n^2)

2)  Hashmap

    Time complexity: O(n)

"""

# This solution uses hashmap

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        
        result = []
        
        hmap = {}
        
        for i in nums1:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1
        
        for i in nums2:
            if i in hmap and hmap[i] > 0:
                hmap[i] -= 1
                result.append(i)
        
        return result

# This is a brute force solution


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        
        result = []
        
        for i in nums1:
            if i in nums2:
                result.append(i)
                nums2.pop(nums2.index(i))
        
        return result


