"""
LeetCode Problem: 895. Maximum Frequency Stack
Link: https://leetcode.com/problems/maximum-frequency-stack/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(1)
Space Complexity: O(N)
"""

class FreqStack:
    def __init__(self):
        self.freqHashMap = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freqHashMap[val] += 1
        
        if self.freqHashMap[val] > self.maxFreq:
            self.maxFreq = self.freqHashMap[val]
        
        self.group[self.freqHashMap[val]].append(val)

    def pop(self) -> int:
        x = self.group[self.maxFreq].pop()        
        self.freqHashMap[x] -= 1
        
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return x