"""
Language: Python
Written by: Mostofa Adib Shakib

Requirement: The array needs to be sorted and bounded

Exponential search involves two steps:
    Find range where element is present
    Do Binary Search in above found range.

How to find the range where element may be present?

The idea is to start with subarray size 1, compare its last element with x, then try size 2, then 4 and so on until last element of a subarray is not greater. 
Once we find an index i (after repeated doubling of i), we know that the element must be present between i/2 and i

Why i/2?

Because we could not find a greater value in previous iteration

Sorted list [7,8,8,8,9]
Target value: 8 

Time and Space Complexity:

Runtime: O(log n) -- logarithmic time

Bounded by the Binary Search which takes log (n) time

Space: O(1) -- Constant Space

Although, Binary Search does require keeping track of 3 indicies, the iterative solution does not typically require any other additional space and can be applied directly on the collection itself, therefore warrants O(1) or constant space.
"""


def exponentialSearch(arr, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    def BinarySearch(arr, low, high, target):

        while low <= high:
            mid = low + (high-low)//2

            if arr[mid] == target:
                return mid

            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

    if arr[0] == target:
        return 0

    index = 1

    n = len(arr)

    while index < n and arr[index] < target:
        index = index * 2

    return BinarySearch(arr, index//2, min(index, n-1), target)


print(exponentialSearch([7,8,8,8,9], 9))