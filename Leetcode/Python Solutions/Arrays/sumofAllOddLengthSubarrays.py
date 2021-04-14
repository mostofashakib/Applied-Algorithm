"""
LeetCode Problem: 1588. Sum of All Odd Length Subarrays
Link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
Further Reading: https://web.stanford.edu/class/cs9/sample_probs/SubarraySums.pdf
Video Explanation: https://www.youtube.com/watch?v=J5IIH35EBVE&t=216s
Language: Python
Written by: Mostofa Adib Shakib

Optimal Solution Explanation:

Consider the subarray that contains A[i], we can take 0,1,2..,i elements on the left,
from A[0] to A[i], we have i + 1 choices.

we can take 0,1,2..,n-1-i elements on the right,
from A[i] to A[n-1], we have n - i choices.

In total, there are k = (i + 1) * (n - i) subarrays, that contains A[i].
And there are (k + 1) / 2 subarrays with odd length, that contains A[i].
And there are k / 2 subarrays with even length, that contains A[i].

A[i] will be counted ((i + 1) * (n - i) + 1) / 2 times for our question.

Example of array [1,2,3,4,5]

1 2 3 4 5 subarray length 1
1 2 X X X subarray length 2
X 2 3 X X subarray length 2
X X 3 4 X subarray length 2
X X X 4 5 subarray length 2
1 2 3 X X subarray length 3
X 2 3 4 X subarray length 3
X X 3 4 5 subarray length 3
1 2 3 4 X subarray length 4
X 2 3 4 5 subarray length 4
1 2 3 4 5 subarray length 5

5 8 9 8 5 total times each index was added, k = (i + 1) * (n - i)
3 4 5 4 3 total times in odd length array with (k + 1) / 2
2 4 4 4 2 total times in even length array with k / 2
"""

# Optimal Solution
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        length = len(arr)
        
        for idx, value in enumerate(arr):
            start = idx + 1
            end = length - idx
            total = ceil((start*end)/2) * value
            result += total
            
        return result


# Brute Force Solution
# Time Complexity: O(N^3)
# Space Complexity: O(1)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        
        length = len(arr)
        k = ceil(length/2)
        i = 0
        total = 0
        
        while k > 0:
            for j in range(length-i):
                total += sum(arr[j:j+i+1])
            i += 2
            k -= 1
        
        return total