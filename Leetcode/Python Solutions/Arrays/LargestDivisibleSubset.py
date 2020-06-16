"""
LeetCode Problem: 368. Largest Divisible Subset
Link: https://leetcode.com/problems/largest-divisible-subset/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n^2)
Space Complexity: O(n)

Explanation:

First of all, notice, that if we need to find 3 numbers given properties, then if we put then in decreasing order a > b > c,
then it is sufficient and enough that a % b = 0 and b % c=0, then it is automatically a % c=0.

Let us know sort our number and in sol[i] list keep the best solution, where the biggest number is equal to nums[i].
How can we find it? Look at all smaller numbers and if nums[i] is divisible by this smaller number, we can update the solution.

Example:

nums = [4,5,8,12,16,20].

    sol[0] = [4], the biggest divisible subset has size 1.
    sol[1] = [5], because 5 % 4 != 0.
    sol[2] = [4,8], because 8 % 4 = 0.
    sol[3] = [4,12], because 12 % 4 = 0.
    sol[4] = [4,8,16], because 16 % 8 = 0 and 16 % 4 = 0 and we choose 8, because it has longer set.
    sol[5] = [4,20] (or [5,20] in fact, but it does not matter). We take [4,20] because it has
    the biggest length and when we see 5, we do not update it.

Finally, the answer is [4,8,16].
"""

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Base case. When the given array is empty

        if len(nums) == 0: return []

        # Sort the given array

        nums.sort()

        # sol array where each element is a subset

        sol = [[num] for num in nums]

         # traverse every element in the array
        for i in range(len(nums)):
            # traverse all the previous elements in the array
            for j in range(i):
                # if the current element is divisible by any of the previous elements the excend the previous subset
                if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                    # this updates the current subset
                    sol[i] = sol[j] + [nums[i]]
                    
        # return the subset which is longest
        return max(sol, key=len)