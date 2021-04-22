"""
Problem Statement: 
    Write a function to crush candy in one dimensional board. In candy crushing games, groups of like
    items are removed from the board. In this problem, any sequence of 3 or more like items should be
    removed and any items adjacent to that sequence should now be considered adjacent to each other.
    This process should be repeated as many time as possible. You should greedily remove characters from left to right.

Language: Python
Written by: Mostofa Adib Shakib

Example 1:

Input: "aaabbbc"
Output: "c"

Explanation:
    1. Remove 3 'a': "aaabbbbc" => "bbbbc"
    2. Remove 4 'b': "bbbbc" => "c"

Example 2:

Input: "aabbbacd"
Output: "cd"

Explanation:
    1. Remove 3 'b': "aabbbacd" => "aaacd"
    2. Remove 3 'a': "aaacd" => "cd"

Example 3:

Input: "aabbccddeeedcba"
Output: ""
Explanation:
    1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
    2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
    3. Remove 3 'c': "aabbcccba" => "aabbba"
    4. Remove 3 'b': "aabbba" => "aaa"
    5. Remove 3 'a': "aaa" => ""

Example 4:

Input: "aaabbbacd"
Output: "acd"
Explanation:
    1. Remove 3 'a': "aaabbbacd" => "bbbacd"
    2. Remove 3 'b': "bbbacd" => "acd"

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque

def candyCrush(string):
  if not string:
    return ""

  queue = deque()
  length = len(string)
  i = 0

  while i < length:
    char = string[i]
    count = 1

    while i < length -1 and char == string[i+1]:
      count += 1
      i += 1

    if queue and queue[-1][0] == string[i]:
      count += queue.pop()[1]
    
    if count < 3:
      queue.append((string[i], count))

    i += 1

  result = ""

  while queue:
    char, count = queue.popleft()

    result += (char * count)

  return result

print("Testing: ", candyCrush("aabbccddeeedcba"))