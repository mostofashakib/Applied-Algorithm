"""
Problem Statement: Given a string, find the deepest string nested inside a '()', '[]' or '{}'."
Language: Python
Written by: Mostofa Adib Shakib

Example: 
    "abc(def)ghi" => ["def"]
    "abc(def[ghi]jkl)mno" => ["ghi"]
    "abc(def)ghi[jkl]mno" => ["def", "jkl"]
    "abc" => []
    "" => []

Time Complexity: O(n)
Space Complexity: O(1)
"""


def maxDepthString(s: str) -> list:
    max_depth = 0
    output = []
    open_brackets = {"(": ")", "{": "}", "[":"]"}
    closing_brackets = {")", "}", "]"}
    
    start_window = 0
    curr_depth = 0
    
    for end_window, c in enumerate(s):
        if c in open_brackets:
            start_window = end_window
            curr_depth += 1
            if curr_depth > max_depth:
                max_depth = curr_depth
                output = []
            
        if c in closing_brackets and c == open_brackets[s[start_window]]:
            output.append(s[start_window +1: end_window])
            curr_depth -= 1
            
    return output