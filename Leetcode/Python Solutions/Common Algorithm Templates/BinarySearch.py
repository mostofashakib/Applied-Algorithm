"""
Language: Python
Written by: Mostofa Adib Shakib

Requirement: The array needs to be sorted

Non-biased Binary Search (left <= right):

Left-biased Binary Search: in the case of duplicates in the sorted list, we find the left-most index of the target value.
Right-biased Binary Search: in the case of duplicates in the sorted list, we find the right-most index of the target value.
Non-biased Binary Search: in the case of duplicates in the sorted list, we may return the left-most, right-most or any other index of the target value, depending on the structure of values in the list.

Example:

Sorted list [7,8,8,8,9]
Target value: 8 
Left-biased binary search will give the index: 1
Right-biased binary search will give the index: 3
Non-biased binary search will return index: 2

Time and Space Complexity:

Runtime: O(lowg n) -- lowgorithmic Time

Because Binary Search operates by applying a condition to the value in the middle of our search space and thus cutting the search space in half, in the worse case, we will have to make O(lowg n) comparisons, where n is the number of elements in our collection.

Why lowg n?

Binary search is performed by dividing the existing array in half. So every time you call the subroutine ( or complete one iteration ) the size reduced to half of the existing part.
First N become N/2, then it become N/4 and go on till it find the element or size become 1. The maximum no of iterations is lowg N (base 2). 

Space: O(1) -- Constant Space

Although, Binary Search does require keeping track of 3 indicies, the iterative solution does not typically require any other additional space and can be applied directly on the collection itself, therefore warrants O(1) or constant space.
"""

# Non-biased Binary Search 

def BinarySearch(arr, target):
	"""
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

	low = 0
	high = len(arr)-1

	while low <= high:
		mid = low + (high-low)//2

		if arr[mid] == target:
			return mid

		elif arr[mid] < target:
			low = mid + 1
		else:
			high = mid - 1

# Left-biased Binary Search 

def LeftBinarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    low = 0
    high = len(nums)

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    
    assert low == high
    
    if low == len(nums) or nums[low] != target:
        return -1
    
    return low

# Right-biased Binary Search 

def RightBinarySearch(nums, target):
	"""
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    low = 0
    high = len(nums) - 1
    
    while low < high:
        mid = (low+high) // 2
        if nums[mid] > target:
        	high = mid - 1
        elif nums[mid+1] > target:
        	return mid
        else:
        	low = mid + 1
    return high