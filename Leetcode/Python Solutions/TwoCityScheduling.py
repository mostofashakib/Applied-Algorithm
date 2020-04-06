"""
LeetCode 1029. Two City Scheduling
Link: https://leetcode.com/problems/two-city-scheduling/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""

Keyword: minimum/maximum = Good candidate for greedy algorithm

Greedy algorithm means taking the locally optimal move at each step which will eventually lead to a globally optimal solution.

The idea is the find the difference between sending one person to city A and city B and then sort the given array in an ascending order.

One key idea to remember is even if city A is cheaper for all the choices we cannot send everyone to city A we will have to send half of the people to city B.

Hence, we send half of the people to the city that costs less(determined by the absolute value) and the other half to the more expensive city.

Algorithm:

Sort the persons in the ascending order by price_A - price_B parameter, which indicates the company additional costs.

To minimise the costs, send n persons with the smallest price_A - price_B to the city A, and the others to the city B.

Time complexityL: O(nlogn)
Space complexity: O(1)

"""


class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        costs.sort(key = lambda x: x[0] - x[1])
        
        length = len(costs)//2
        
        result = 0
        
        for i in range(length):
            result += costs[i][0] + costs[i+length][1]
        
        return result