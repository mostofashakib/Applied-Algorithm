"""
LeetCode Problem: 739. Daily Temperatures
Link: https://leetcode.com/problems/daily-temperatures/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = []
        stack = []                                              # Initializes a stack
        N = len(T)
        
        result = [0]*N                                          # Initializes an array
        
        # Traverse the string backwards
        for i in range(N-1, -1, -1):
            num = T[i]
            
            # If the stack is not empty
            if stack:
                # Since the value at the top of the stack is greater than the current value
                # The difference is recorded in the result array
                # Push the current value on the stack along with it's index
                if num < stack[-1][0]:
                    result[i] = stack[-1][1]-i
                    stack.append([num, i])
                
                else:
                    # We keep poping values off the stack until the stack is either empty or the value
                    # at the top of the stack is greater than the current value

                    while stack and num >= stack[-1][0]:
                        stack.pop()
                    
                    # Since the value at the top of the stack is greater than the current value
                    if stack:
                        result[i] = stack[-1][1]-i              # The difference is recorded in the result array
                        stack.append([num, i])                  # Push the current value on the stack along with it's index
   
                    else:
                        stack.append([num, i])                  # No day is warmer than the current day 
                        result[i] = 0                           # Push the current value on the stack along with it's index

            # If the stack is empty
            else:
                result[i] = 0                                   # No day is warmer than the current day
                stack.append([num, i])                          # Push the current value on the stack along with it's index
        
        return result