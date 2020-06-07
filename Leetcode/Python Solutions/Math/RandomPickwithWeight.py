"""
LeetCode Problem 528. Random Pick with Weight

Link: https://leetcode.com/problems/random-pick-with-weight/
Written by: Mostofa Adib Shakib
Language: Python

Example: 

Array = [1, 9]

When we pick up a at random number out of it, the chance is that 9 times out of 10 we would pick the number 9.
In other words, the probability that a number got picked is proportional to the value of the number, with regards to the total sum of all numbers.

Explanation:

Algorithm:

For the __init__() function:

1) We generate a list of prefix sums from a given list of numbers.
2) We keep track of the total sum of the input numbers, so that later we could use this total sum to scale up the random number.

For the pickIndex() function,:

1) We generate a random number between 0 and 1. We then scale up this number, which will serve as our target offset.
2) We then scan through the prefix sums that we generated before by linear search, to find the first prefix sum that is larger than our target offset.
3) The index of this prefix sum would be exactly the right place that the target should fall into. Hence, we return the index

"""

# Solution 1: Inefficient Solution - Linear Search
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.array = []
        self.total = 0
        for i in self.w:
            self.total += i
            self.array.append(self.total)
        
    def pickIndex(self) -> int:
        target = random.random() * self.total
        
        for index, value in enumerate(self.array):
            if target < value:
                return index

# Solution 2: Efficient Solution - Binary Search
# Time Complexity: O(n)
# Space Complexity: O(logn)

class Solution:
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low