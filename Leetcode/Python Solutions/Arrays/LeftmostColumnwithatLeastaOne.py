"""
LeetCode 30 Day challenge.Leftmost Column with at Least a One
Link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""
Approach 1  Fastest - Zipzag traversal of a matrix
Time Complexity: O(n)
Space Complexity: O(1)
"""


def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    rows, cols = binaryMatrix.dimensions()
    
    current_cols = cols -1
    current_rows = 0
    
    while current_rows < rows and current_cols >= 0:
        if binaryMatrix.get(current_rows, current_cols) == 1:
            current_cols -= 1
        else:
            current_rows += 1
            
    if current_cols != cols-1:
        return current_cols + 1
    else:
        return -1

"""
Approach 2: Fast - Binary Search
Time Complexity: O(n)
Space Complexity: O(1)
"""

def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    
    rows, cols = binaryMatrix.dimensions()
    
    def hasOne(column):
        return any(binaryMatrix.get(i, column) for i in range(rows))
    
    low = 0
    high = cols
    
    while low < high:
        mid = (low + high) // 2
        if hasOne(mid):
            high = mid
        else:
            low = mid + 1
    return low if low < cols else -1


"""
Approach 3: Brute Force - Timed out
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    
    rows, cols = binaryMatrix.dimensions()

    matrix = [[-1 for i in range(rows)] for j in range(cols)]
    
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            matrix[j][i] = binaryMatrix.get(i,j)
    
    for i in range(rows):
        if sum(matrix[i]) < 1:
            count += 1
        else:
            return count

    return -1
