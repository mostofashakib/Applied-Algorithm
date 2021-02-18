"""
Kth-largest/Kth-smallest

Algorithm Name: QuickSelect - Hoare's selection algorithm
Language: Python
Written by: Mostofa Adib Shakib

Space Complexity: O(1) - In-Place Algorithm

Time Complexity:
    Best/Average case: O(n)
    Worst case: O(n^2)

    The Worst case happens when we want to find the maximum in a sorted array and we always 
    choose the first element to be the pivot.

Algorithm:
    1) Choose a pivot value at random: We generate a random number in the range[firstIndex, lastIndex]
    2) Partition the array: Rearrange the list in a way that all the elements less than the pivot
    are on the left side of the pivot and all the elements more than the pivot are on the right side
    of the pivot. Then return the index of the pivot element
    3) Instead of recusing into both sides, we just take the side where the number of interest lies.

Three cases after partitioning:
    1) K == Pivot: It means that we have found the kth-smallest item.
    2) K < Pivot: The kth-smallest item is on the left side of the pivot, that's why we discard the right subarray.
    3) K > Pivot: The kth-smallest item is on the right side of the pivot, that's why we discard the left subarray.

Things to note:
    After partitioning the pivot is on it's perfect position in the ascending sorted array.
"""

# QuickSelect to find the K-th smallest element in an array.

def findKthSmallest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """ 
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]

        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
        
        # 2. move all smaller elements to the left
        store_index = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]  
        
        return store_index
    
    def select(left, right, k_smallest):
        """
        Returns the k-th smallest element of list within left..right
        """
        if left == right:       # If the list contains only one element,
            return nums[left]   # return that element
        
        # select a random pivot_index between 
        pivot_index = random.randint(left, right)     
                        
        # find the pivot position in a sorted list   
        pivot_index = partition(left, right, pivot_index)
        
        # the pivot is in its final sorted position
        if k_smallest == pivot_index:
             return nums[k_smallest]
        # go left
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        # go right
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(nums) - 1, k)

