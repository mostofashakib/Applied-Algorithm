"""
LeetCode Problem: 752. Open the Lock
Link: https://leetcode.com/problems/open-the-lock/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N^2 ∗ A^N + D)
Space Complexity: O(A^N + D)
"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = set('0000')

        while queue:
            string, steps = queue.popleft()
            
            if string == target:
                return steps
            
            if string not in dead_set:                
                for i in range(4):
                    digit = int(string[i])
                    
                    for move in [-1, 1]:
                        newDigit = (digit + move) % 10
                        newString = string[:i] + str(newDigit) + string[i+1:]
                        
                        if newString not in visited:
                            visited.add(newString)
                            queue.append((newString, steps+1))
        return -1