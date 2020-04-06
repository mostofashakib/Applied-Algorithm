"""
890 Leetcode. Find and Replace Pattern
https://leetcode.com/problems/find-and-replace-pattern/
"""


"""
This program uses a dictionary to get 


"""

"""
Solution 1: This uses a helper function to see if two words have a match or not.
"""

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(w,p):
            return len(set(w)) == len(set(p)) == len(set(zip(w,p)))
        
        res = []
        for w in words:
            if match(w, pattern):
                res.append(w)
        return res

"""
Solution 2: This uses a dictonary to see if two words have a match or not.
"""

def findAndReplacePattern(self, words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """
    def match(w,p):
        d = {}
        if len(w) != len(p):
            return False
        for a,b in zip(w,p):
            if a not in d:
                if b in d.values():
                    return False
                d[a] = b
            else:
                if b != d[a]:
                    return False
        return True

    res = []

    for w in words:
        if match(w, pattern):
            res.append(w)
    return res