"""
205 Leetcode. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/
"""


"""
This program uses a dictionary to get 


"""


def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    if len(s) != len(t):
        return False
    
    hmap = {}
    
    for i,j in zip(s,t):
        if i not in hmap:
            if j in hmap.values():
                return False
            hmap[i] = j
        else:
            if j != hmap[i]:
                return False
    return True