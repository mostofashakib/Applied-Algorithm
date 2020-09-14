"""
Educational Codeforces Round 32. B. Buggy Robot
Link: https://codeforces.com/contest/888/problem/B
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input())
s = input()
left = 0
right = 0
up = 0
down = 0
 
for i in s:
    if i == "U":
      up += 1
    elif i == "D":
      down += 1
    elif i == "L":
      left += 1
    else:
      right += 1
 
print(2*min(left, right) + 2*min(up, down))