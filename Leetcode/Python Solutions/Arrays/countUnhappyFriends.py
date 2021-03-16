"""
LeetCode Problem: 1583. Count Unhappy Friends
Link: https://leetcode.com/problems/count-unhappy-friends/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N^3)
Space Complexity: O(N)
"""

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        ans = 0
        hashMap = defaultdict(int)
        
        # Pair map for easy reference to the member in the same pair
        for pair in pairs:
            hashMap[pair[0]] = pair[1]
            hashMap[pair[1]] = pair[0]
        
        # Iterate each person(p)
        for p in range(n):
            y = hashMap[p]
            yIndex = preferences[p].index(y)
            
            # Iterate every other on person(p)'s preference list in front of pair member(y)
            for u in preferences[p][:yIndex]:
                # Compare the preference ranking of p and other's current pairing(v) on other's preference list
                if preferences[u].index(p) < preferences[u].index(hashMap[u]):
                    ans += 1 
                    break
        
        return ans