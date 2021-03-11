"""
Language: Python
Written by: Mostofa Adib Shakib
Video Explanation: https://www.youtube.com/watch?v=CWDQJGaN1gY
Further Reading: https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
                 https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/

Binary Index Tree or Fenwick Tree

The size of the BITree is one more than the size of the input array

Time Complexity:
    Construction: O(nlogn)
    Update BIT: O(logn)
    Get Sum (0 to n): O(logn)

getParent:
    => Find 2's complement
    => "AND" the previous numbr with the original number
    => "Subtract" the previous number from the original number

getSum:
    => Find 2's complement
    => "AND" the previous numbr with the original number
    => "Add" the previous number from the original number
"""

# Returns sum of arr[0..index]. This function assumes 
# that the array is preprocessed and partial sums of 
# array elements are stored in BITree[].

def getsum(BITree, idx): 
    ans = 0 #initialize result 
  
    # index in BITree[] is 1 more than the index in arr[] 
    idx = idx + 1
  
    # Traverse ancestors of BITree[index] 
    while idx > 0: 
  
        # Add current element of BITree to sum 
        ans += BITree[idx] 
  
        # Move index to parent node
        idx -= idx & (-idx)

    return ans
  
# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and 
# all of its ancestors in tree.

def updatebit(BITree , n , idx , value): 
  
    # index in BITree[] is 1 more than the index in arr[] 
    idx += 1
  
    # Traverse all ancestors and add 'val' 
    while idx <= n: 
  
        # Add 'val' to current node of BI Tree 
        BITree[idx] += value 
  
        # Update index to that of parent in update View 
        idx += idx & (-idx) 
  
  
# Constructs and returns a Binary Indexed Tree for given array of size n. 
def construct(arr, n): 
  
    # Create and initialize BITree[] as 0 
    BITree = [0]*(n+1) 
  
    # Store the actual values in BITree[] using update() 
    for idx in range(n): 
        updatebit(BITree, n, idx, arr[idx]) 
  
    return BITree