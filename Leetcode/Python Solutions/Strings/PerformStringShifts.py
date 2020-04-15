"""
LeetCode 30 Day Challenge: Perform String Shifts
Link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/
Written by: Mostofa Adib Shakib
Language: Python

Cutting and slicing strings in Python
array[0]    = The left most character in the array
array[-1]   = The right most character in the array
array[n:]   = Start from the character at index n
array[:n]   = End up to but not including the character at index n

Example: 

array[3:8]   = Start at index 3 and end at index 7
"""


"""
N = Length of the string
L = Length of the shift array

Time Complexity: O(N*L)
Space Complexity: O(N)
"""

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        string = s
        
        def leftShift(text,n):
            return text[n:] + text[:n]
        def rightShift(text,n):
            return text[-n:] + text[:-n]
        
        for i in shift:
            if i[0] == 0:
                string = leftShift(string, i[1])
            else:
                string = rightShift(string, i[1])
                
        return string

"""
Approach 2: Compute Net Shift - Faster 
Time Complexity: O(N+L)
Space Complexity: O(N)
"""

class Solution:
    def stringShift(self, string: str, shift: List[List[int]]) -> str:
        
        # Add up the left shifts and right shifts.
        overall_shifts = [0, 0]
        for direction, amount in shift:
            overall_shifts[direction] += amount
        left_shifts, right_shifts = overall_shifts
        
        # Determine which shift (if any) to perform.
        if left_shifts > right_shifts:
            left_shifts = (left_shifts - right_shifts) % len(string)
            string = string[left_shifts:] + string[:left_shifts]        # Left Shift
        else:
            right_shifts = (right_shifts - left_shifts) % len(string)
            string = string[-right_shifts:] + string[:-right_shifts]    # Left Shift

        return string