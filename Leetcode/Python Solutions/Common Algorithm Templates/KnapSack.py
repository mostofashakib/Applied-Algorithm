import collections

"""
Language: Python
Written by: Mostofa Adib Shakib

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

Items = collections.namedtuple('Item', ('weight', 'value'))

def optimum_subject_to_capacity(self, items, capacity):
    v = [ [-1] * (capacity +1) for _ in items ]          # initializing the matrix

    return self.optimum_subject_to_item_adn_capacity(len(items)-1, capacity)

def optimum_subject_to_item_adn_capacity(self, k, available_capacity):
    if k < 0: return 0      # Base case

    if self.v[k][available_capacity] == -1:
        without_curr_item = self.optimum_subject_to_item_adn_capacity(k-1, available_capacity)    # finds the maximum value without the current item
        
        # finds the maximum value with the current item hence the capacity decreases
        with_curr_item = 0 if available_capacity < self.items[k].weight else self.optimum_subject_to_item_adn_capacity(k-1, available_capacity - self.items[k].weight)
        
        self.v[k][available_capacity] = max(without_curr_item, with_curr_item)  # change the value of the matrix

        return self.v[k][available_capacity]  # returns the answer