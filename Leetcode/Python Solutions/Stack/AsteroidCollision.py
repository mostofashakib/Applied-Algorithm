"""
LeetCode Problem: 735. Asteroid Collision
Link: https://leetcode.com/problems/asteroid-collision/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # If there are no asteroids or the number of asteroids is 1 then return the input array
        if  len(asteroids) < 2: return asteroids
        
        stack = []                              # Initializes a stack
        
        # Traverse through the input array

        for num in asteroids:
            # If the stack is empty or the num is positive then append to the stack
            if not stack or num > 0:
                stack.append(num)
            # If the element at the top of the stack is negative then append to num to the stack
            elif stack[-1] < 0:
                stack.append(num)
            # If the top of the stack is positive and num is negative
            else:
                while True:
                    # If the element at the top of the stack and num have the same magnitude then both should be discarded
                    if stack[-1] == -num:
                        stack.pop()
                        break
                        
                    # If the element at the top of the stack has a higher magnitude than num then just discard num
                    elif stack[-1] > -num:
                        break

                    # If the element at the top of the stack has a lower magnitude than num and both of them are negative
                    # that means they are moving in the same direction hence num is appended to the stack 
                    elif stack[-1] < -num and stack[-1] < 0 and num < 0:
                        stack.append(num)
                        break

                    # If the element at the top of the stack has a lower magnitude than num and at least one of them is negative
                    # that means they are moving in opposite direction hence we pop the element at the top of the stack and continue
                    # until the element at the top of the stack either has a higher magnitude, equal magnitude or the stack is empty.
                    elif stack[-1] < -num:
                        stack.pop()
                        
                        if not stack:
                            stack.append(num)
                            break                        
        return stack