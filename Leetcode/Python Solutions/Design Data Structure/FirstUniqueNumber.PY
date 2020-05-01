"""
LeetCode 30 day Challenge. First Unique Number
Link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3313/
Language: Python
Written by: Mostofa Adib Shakib

Amortised Time Complexity: O(1)
Space Complexity: O(n)

Things to note:
1) Deque does not contain duplicates and is used to preserve the order in which they were inserted
2) Hashmap is used to count the frequency of occurance of each element which is used to figure out
which elements has duplicate entries.
"""

from collections import deque

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.hashmap = {}
        self.queue = deque()
        
        for i in nums:
            if i not in self.hashmap:
                self.hashmap[i] = 1
                self.queue.append(i)
            else:
                self.hashmap[i] += 1

    def showFirstUnique(self) -> int:
        
        while len(self.queue) > 0 and self.hashmap[self.queue[0]] > 1:
            self.queue.popleft()
            
        if len(self.queue) == 0: return -1
        
        return self.queue[0]
        

    def add(self, value: int) -> None:
        if value not in self.hashmap:
            self.hashmap[value] = 1
            self.queue.append(value)
        else:
            self.hashmap[value] += 1
        

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)