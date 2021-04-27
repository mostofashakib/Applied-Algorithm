"""
LeetCode Problem: 340. Longest Substring with At Most K Distinct Characters
Link: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(nk)
Space Complexity: O(k)
"""

# Sliding Window + HashMap

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        
        if n * k == 0:
            return 0
        
        hashMap = defaultdict(int)
        maxLength = 0
        left = 0
        right = 0
        
        while right < n:
            char = s[right]
            
            hashMap[char] = right
            right += 1
            
            if len(hashMap) > k:
                idx = min(hashMap.values())
                del hashMap[s[idx]]
                
                left = idx + 1
                
            maxLength = max(maxLength, right - left)
            
        return maxLength