"""
1079 Leetcode. Letter Tile Possibilities
https://leetcode.com/problems/letter-tile-possibilities/
"""

"""



"""

class Solution:
    def numTilePossibilities(self, tiles):
    	"""
        :type tiles: str
        :rtype: int
        """
        counts = {}
        for t in tiles:
            if t not in counts:
                counts[t] = 1
            else:
                counts[t] += 1
        return self.dfs(counts)

    def dfs(self, counts):
        sum = 0
        for c in counts:
            if counts[c] > 0:
                counts[c] -= 1
                sum += 1
                sum += self.dfs(counts)
                counts[c] += 1                 # backtrack
        return sum