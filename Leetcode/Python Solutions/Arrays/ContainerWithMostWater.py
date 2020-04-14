"""
LeetCode Problem 111. Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)

we need to take the minimum of the two heights
Traverse two pointers one from the left hand side and one from the righthand side
MaxWater = Maximum amount of water
HeightSmall = height of the smallest buidling
MaxWidth = length between the highestBuildingFromLeft & highestBuildingFromRight
MaxWater =  HeightSmall * MaxWidth
Time complexity: O(n)
Space complexity: O(1)

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:        
        
        HighestBuildingFromLeft = 0
        HighestBuildingFromRight = len(height) - 1
        ans = 0
        
        while HighestBuildingFromLeft < HighestBuildingFromRight:
            HeightSmall = min(height[HighestBuildingFromLeft], height[HighestBuildingFromRight])
            MaxWidth =  HighestBuildingFromRight - HighestBuildingFromLeft
            MaxWater =  HeightSmall * MaxWidth
            ans = max(ans, MaxWater)
            
            if height[HighestBuildingFromLeft] < height[HighestBuildingFromRight]:
                HighestBuildingFromLeft += 1
            else:
                HighestBuildingFromRight -= 1
        
        return ans