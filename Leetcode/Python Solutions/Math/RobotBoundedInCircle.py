"""
LeetCode Problem: 1041. Robot Bounded In Circle
Link: https://leetcode.com/problems/robot-bounded-in-circle/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # direction = N => 0, W => 1, S => 2, E => 3
        
        x_coordinate = 0
        y_coordinate = 0
        direction = 0
        
        for instruction in instructions:
            if instruction == "G":
                if direction == 0:
                    y_coordinate += 1
                elif direction == 1:
                    x_coordinate -= 1
                elif direction == 2:
                    y_coordinate -= 1
                else:
                    x_coordinate += 1
                    
            elif instruction == "L":  # Anticlockwise rotation
                direction += 1
                
            else:
                direction -= 1        # Clockwise rotation
            
            # This makes sure that the direction value is between 0 and 3
            direction = (direction)%4
            
        # if the robot comes back to origin or it's direction is different from it's initial direction
        if (x_coordinate == 0 and y_coordinate == 0) or direction != 0:
            return True
        else:
            return False