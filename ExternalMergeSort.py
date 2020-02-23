# LC discussion Bloomberg Phone Screen
# https://leetcode.com/discuss/interview-question/346748/Bloomberg-or-Phone-Screen-or-File-Diffs-With-Ram-Constraints

"""
Question: 

You have two files, each of 100TB in size. Each file is composed of trades that take up one line each.
Each trade has a unique key. You have 1 megabyte of RAM. Print out the lines to an output file that
are in file A but not file B as well as the lines that are in file B but not in file A.

"""


"""

Algorithm:

Sort file A using external sort (merge sort, works the best). Write it back to the disk.
Sort file B using external sort (merge sort, works the best). Write it back to the disk.
Retrieve first block of A and B where size(blockA) + size(blockB) < 1MB.
Run two pointers on A and B respectively. Compare A against B. If a matching value in B isn't found then output it to screen / store in another data structure. (be vary about 1MB)
Repeat for all the blocks in A and B. This wouldn't take more than linear time.
m = len(A), n = len(B)
N = m + n

Time complexity:
O(mlogm) + O(nlogn) + O(m+n) ~ O(NlogN) [Asymptotically]

Space complexity:
O(N)

"""