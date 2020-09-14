"""
Language: Python
Written by: Mostofa Adib Shakib
Reading Material: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
Video Material: 


Problem Statement: A thief breaks into a clock store. Each clock has a weight and a value which are known to the thief. His knapsack cannot hold more than a
specified combined weight. His intention is to take clocks whose total value is maximum subject to  the knapsack's weight constraint.

Data format Item, (weight, value)

A: 20oz, 65$             I: 30oz, 120$
B: 8oz , 35$             J: 65oz, 320$
C: 60oz, 245$            K: 75oz, 75$
D: 55oz, 195$            L: 10oz, 40$
E: 40oz, 65$             M: 95oz, 200$
F: 70oz, 150$            N: 50oz, 100$
G: 85oz, 275$            O: 40oz, 220$
H: 25oz, 155$            P: 10oz, 99$

Dynamic Programming

1) Optimal Substructure:
    To consider all subsets of items, there can be two cases for every item:
     (1) the item is included in the optimal subset
     (2) not included in the optimal set.
Therefore, the maximum value that can be obtained from n items is max of following two values.
1) Maximum value obtained by n-1 items and W weight (excluding nth item).
2) Value of nth item plus maximum value obtained by n-1 items and W minus weight of the nth item (including nth item).

If weight of nth item is greater than W, then the nth item cannot be included and case 1 is the only possibility.

2) Overlapping Subproblems
Following is recursive implementation that simply follows the recursive structure mentioned above.

Algorithm:

By recusively calling the function subproblems can be solved with the following choices

1) Find the optimum solution if a given clock is choosen
2) Find the optimum solution if a given clock is not choosen

At the end return the maximum value of the two values.

Time complexity: O(m*n)
Space Complexity: O(m*n)

"""

# Recursive Solution + Memoization
# Time Complexity: O(capacity+n)
# Space Complexity: O(capacity+n)

def knapSack(capacity, weights, values, n, memo):
    # Base Case
    if n < 0 or capacity == 0:
        return 0
    # If the number was calculated previously
    if memo[n][capacity] != -1: 
        return memo[n][capacity]

    # If the capacity is less than the weight of the item then there is only one possibility
    # Don't include this item in the answer set and move to the next item
    if capacity < weights[n]:
        memo[n][capacity] = knapSack(capacity, weights, values, n-1, memo)
        return memo[n][capacity]
    # If the capacity is more than or equal to the weight then there are two possibilities
    # Either we include the item to the answer set or we do not. We take the maximum of both
    else:
        memo[n][capacity] = max(values[n] + knapSack(capacity-weights[n], weights, values, n-1, memo), knapSack(capacity, weights, values, n-1, memo))
        return memo[n][capacity]


# Dynamic Programming
# Time Complexity: O(capacity+n)
# Space Complexity: O(capacity+n)

def knapSack(capacity, weights, values, n):
    # Dynamic Programming table
    dp = [ [0 for i in range(capacity+1)] for j in range(n+1) ]

    for currentItem in range(1, n+1):
        for currentCapacity in range(1, capacity+1):
            # If the weight of the item is more than the current capacity. There is only one possibility
            if weights[currentItem-1] > currentCapacity:
                dp[currentItem][currentCapacity] = dp[currentItem-1][currentCapacity]
            # Otherwise there are two possibilities and we take the maximum
            else:
                dp[currentItem][currentCapacity] = max(dp[currentItem-1][currentCapacity], values[currentItem-1] + dp[currentItem-1][currentCapacity-weights[currentItem-1]])

    return dp[-1][-1]