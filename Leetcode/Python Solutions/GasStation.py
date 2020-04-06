"""
LeetCode Problem: 134. Gas Station
Link: https://leetcode.com/problems/gas-station/
Language: Python
Written by: Mostofa Adib Shakib

Observations:
    1) If the sum of gas is less than the sum of costs then we will not be able to complete the circle so return -1
    2) If the costs to travel to the next station is more than gas at the starting station then it cannot be the starting station

Time Compplexity: O(n)
Space Complexity: O(1)

"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):    # if sum(gas) is less then sum(costs) then return -1
            return -1
        
        n = len(gas)                # length of the array
        curr_tank = 0               # current level of gas
        starting_station = 0        # starting station
        
        for i in range(n):          # loops over the array
            curr_tank += gas[i] - cost[i]         # finds the remaining gas if the car travels to the next gas station
            if curr_tank < 0:                     # if the value is negetive then the current station cannot be the starting station
                starting_station = i +1           # changes the index of the starting gas station
                curr_tank = 0                     # resets the level of gas
                
        return starting_station                   # returns the index of the starting gas station
