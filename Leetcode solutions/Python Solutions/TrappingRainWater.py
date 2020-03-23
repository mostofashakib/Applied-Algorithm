"""
LeetCode Problem: 42. Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/
Written by: Mostofa Adib Shakib
Language: Python

Observation:

1) The height of the building is increasing up until the maximum height of the buildings
2) The height of the building is decreasing from the maximum height of the building till the end

Algorithm:

1) Find the maximum height of the building
2) call the function twice for both the parts and for each part
    find the maximum height seen so far and if the index of the current building is smaller than the maximum height seen so far
    then find the difference and increment the value of the partial_sum.
3) return the value of the two partial_sums in order to get the total rainwater trapped

Time Complexity: O(n)
Space Complexity: O(1)

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0     #edge case
        
        max_h = height.index(max(height))   # gets the index of the maximum height
        
        # call the function from the first index till the index of the building with the maximum height 
        # call the function from the last index till the index of the building with the maximum height.
        return self.getPartialSum(height[:max_h]) + self.getPartialSum(reversed(height[max_h+1:]))  
        
    def getPartialSum(self, height):
        partial_sum = 0   # keeps track of the amount of trapped rain
        max_height_seen_so_far = float('-inf')   # keeps track of the maximum height seen so far
         
        for i in height:   #traverses through the array 
            if i >= max_height_seen_so_far:  # if the height of the current building is greater than or equal to the maximum height seen so far then update
                max_height_seen_so_far = i
            else:
                partial_sum += max_height_seen_so_far - i # else update the value of partial_sum with
                                                          #  the difference between the maximum height and the height of the current building
        return partial_sum   # returns the total volume of trapped water
