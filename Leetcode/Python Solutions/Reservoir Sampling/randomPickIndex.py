"""
LeetCode Problem: 398. Random Pick Index
Link: https://leetcode.com/problems/random-pick-index/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(1)

Explanation:

Draw the 1st number. If there is a second number, then we will hold 1st number by probability = 1/2, and
replace the 1st number with the 2nd number with probability = 1/2. After this step suppose number is now X.
If there is 3rd number, then we will hold the X with probability = 2/3 and replace X with the 3rd number with
probability = 1/3. Why do they hold the same probability to be picked?

Because:

Probability that the 3rd number is picked = 1/3
Probability that the 2nd number is picked = 1 * 1/2 * 2/3 = 1/3
Probability that the 1st number is picked = 1 * 1/2 * 2/3 = 1/3

If nums[i] == target, we can pick the other number with probability = 1/(n+1), or keep original number
with probability = n/(n+1). Hence we can guarantee that each number is picked with probability = 1/(n+1)
"""

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def pick(self, target: int) -> int:
        count = 0
        res = None
        
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                chance = random.randint(1, count)
                
                if chance == count:
                    res = i
        return res