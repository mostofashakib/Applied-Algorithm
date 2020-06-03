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

"""

"""
Solution 1: Constant Space
Time complexityL: O(nlogn)
Space complexity: O(1)
"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        number = len(costs)
        cityA = int(number/2)
        cityB = int(number/2)
        result = 0
            
        costs = sorted(costs, key = lambda x: abs(x[0] - x[1]), reverse = True)

        for i in range(len(costs)):
            if costs[i][0] < costs[i][1] and cityA > 0:
                cityA -= 1
                result += costs[i][0]
            elif costs[i][1] < costs[i][0] and cityB > 0:
                cityB -= 1
                result += costs[i][1]
                
            elif cityA == 0:
                cityB -= 1
                result += costs[i][1]
                
            elif cityB == 0:
                cityA -= 1
                result += costs[i][0]
                
        return result

"""
Solution 2: Linear Space
Time Complexity: O(NlogN)
Space Complexity: O(n)
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        number = len(costs)
        cityA = int(number/2)
        cityB = int(number/2)
        result = 0
        array = []
        
        for i in range(len(costs)):
            diff = abs(costs[i][0]-costs[i][1])
            array.append([costs[i], diff, i])
            
        array = sorted(array, key = operator.itemgetter(1), reverse = True)

        for i in range(len(array)):
            if array[i][0][0] < array[i][0][1] and cityA > 0:
                cityA -= 1
                result += array[i][0][0]
            elif array[i][0][1] < array[i][0][0] and cityB > 0:
                cityB -= 1
                result += array[i][0][1]
                
            elif cityA == 0:
                cityB -= 1
                result += array[i][0][1]
                
            elif cityB == 0:
                cityA -= 1
                result += array[i][0][0]
                
        return result