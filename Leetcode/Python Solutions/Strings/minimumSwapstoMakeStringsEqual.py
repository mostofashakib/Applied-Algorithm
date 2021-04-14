"""
LeetCode Problem: 1247. Minimum Swaps to Make Strings Equal
Link: https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)

Explanation:

1) Use "x_y" when x in s1 at index i and y in s2 at same index i. 
2) Use "y_x" when y in s1 at index j and x in s2 at same index j.

Example 1:
s1 = "xx"
s2 = "yy"

Iterate through both strings and check every index if we get two indexes with different values in both s1 and s2:
"x_y" at index 0 and "x_y" at index 1. if we have 2 "x_y" then we only need 1 swap to make them equal.
Swap x at index 0 in s1 with y at index 1 in s2.

Example 2:
s1 = "yy"
s2 = "xx"

We have 2 different values: "y_x" at index 0 and "y_x" at index 1. so it will also take 1 swap to make them equal.

Example 3:
s1 = "xy"
s2 = "yx"

Here we have one count of "x_y" at index 0 and one count of "y_x" at index 1. We need 2 swaps to make these indexes equal.
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".

Example 4:
s1 = "xxyyxyxyxx",
s2 = "xyyxyxxxyx"

First remove the indexes with same characters:
s1 = "xyxyyx"
s2 = "yxyxxy"

"x_y" count = 3 (index 0, 2, 5)
"y_x" count = 3 (index 1, 3, 4)

index 0 and 2 can be made equal in just 1 swap. see Example 1.
index 1 and 3 can also be made equal in just 1 swap. see Example 2.
index 5 and 4 can be made Equal in 2 swaps. see Example 3

so we only need 4 swaps.

Steps:
	1) Get the count of "x_y" and "y_x"
	2) If sum of both counts is odd then return -1. We need a pair to make the strings equal
	3) Each 2 count of "x_y" needs just 1 swap. So add half of "x_y" count to the result
	4) Each 2 count of "y_x" needs just 1 swap. So add half of "y_x" count to the result
	5) If we still have 1 count of "x_y" and 1 count of "y_x" then they need 2 swaps so add 2 in result.

"""

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1
        
        countXY = 0
        countYX = 0
        
        for i in range(len(s1)):
            if s1[i] == "x" and s2[i] == "y":
                countXY += 1
            elif s1[i] == "y" and s2[i] == "x":
                countYX += 1
                
        ans = countXY//2 + countYX//2
        
        if countXY % 2 == 0 and countYX % 2 == 0:
            return ans
        elif (countXY + countYX) % 2 == 0:
            return ans + 2
        else:
            return -1