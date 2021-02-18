"""
LeetCode Problem: 621. Task Scheduler
Link: https://leetcode.com/problems/task-scheduler/
Language: Python
Written by: Mostofa Adib Shakib
Time Complexity: O(n)
Space Complexity: O(n)

Explanation:

1. tasks = ["A","A","A","B","B","B"], n = 2
A B X
A B X
A B

answer = 8 (3 * 2 + 2)

2. tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
A B C
A D E
A F G
A X X
A X X
A

answer = 16 (5 * 3 + 1)

3. tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], n = 2
A B C D E
A B C D A
B C 

answer = 12 (no idle time so this is just len(tasks))

Geneneralization,

Formula = Max of either ( (frequency of the max task - 1) * (n + 1) ) + last_row or len(tasks)

last_row = count of max frequency tasks
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        
        for task in tasks:
            if task not in hashmap:
                hashmap[task] = 1
            else:
                hashmap[task] += 1
                
        mFreq = max(hashmap.values())
        lastRow = 0
        
        for task in hashmap.values():
            if mFreq == task:
                lastRow += 1
        
        possibleCPUTime = (mFreq-1) * (n+1) + lastRow
        
        return max(possibleCPUTime, len(tasks))