"""
LeetCode Problem: 582. Kill Process
Link: https://leetcode.com/problems/kill-process/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = defaultdict(list)
        
        for child_idx, parent_pid in enumerate(ppid):
            child_pid = pid[child_idx]
            children[parent_pid].append(child_pid)
        
        result = [kill]
        stack = [kill]
        
        while stack:
            pid = stack.pop()
            result.extend(children[pid])
            stack.extend(children[pid])
            
        return result