"""
LeetCode Problem #128. Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Language: Python
Written by: Mostofa Adib Shakib

Algorithm:

The numbers are stored in a HashSet to allow O(1) lookups, and we only attempt to build sequences from numbers that are not already part
of a longer sequence. This is accomplished by first ensuring that the number that would immediately precede the current number in a
sequence is not present, as that number would necessarily be part of a longer sequence.

Time Complexity: O(n)
Space Complexity: O(n)

Time Complexity Analysis:

Although the time complexity appears to be quadratic due to the while loop nested within the for loop,
closer inspection reveals it to be linear. Because the while loop is reached only when currentNum marks the beginning of a sequence
(i.e. currentNum-1 is not present in nums), the while loop can only run for n iterations throughout the entire runtime of the algorithm.
This means that despite looking like O(n⋅n) complexity, the nested loops actually run in O(n + n) = O(n) time.
All other computations occur in constant time, so the overall runtime is linear.
"""

# Approach #1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashSet = set(nums)
        ans = 0
        length = len(nums)
        visited = set()
        
        for i in range(length):
            currL = currR = nums[i]
            streak = 1
            
            while currL-1 in hashSet and (currL-1) not in visited:
                visited.add(currL-1)
                streak += 1
                currL -= 1
                
            
            while currR+1 in hashSet and (currR+1) not in visited:
                visited.add(currR+1)
                streak += 1
                currR += 1
            
            ans = max(ans, streak)
            
        return ans

# Approach #2

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak