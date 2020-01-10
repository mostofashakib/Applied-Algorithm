"""
LeetCode Problem: 45. Jump Game II
Link: https://leetcode.com/problems/jump-game-ii/
Language: Python
Written by: Mostofa Adib Shakib
"""

#Dynamic Programming[Top Down Method]

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Dynamic Programming[Top Down Method]
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        
        Formula:
        minJumps(start, end) = Min ( minJumps(k, end) ) for all k reachable from start
        
        
        An element's position is good if it is possible to reach the start index from that position
        and if it is also possible to reach the end from the element's position.
        """
        n = len(nums)            # finds the length of the array
        if n == 0 or nums[0] == 0: return 0     # edge cases
        
        memo = [0 for i in range(n)]     # lookup array
        memo[0] = 0   # the minimum step to go from 0th element to 0th element is always 0
        
        for i in range(1, n):          # traverses the array
            memo[i] = float('inf')     # assings a maximum value to check if it's a good position or not
            for j in range(i):         # checks to see if a certain position can be reached from the start
                if i <= j + nums[j] and memo[j] != float('inf'):  # checks to see if the jump falls within jump range
                    memo[i] = min(memo[i], 1+ memo[j])    # sets the minimum jump to get to a certain position
                    break                                 # break from the loop if a good position is found
                    
        return memo[-1]   # returns the minimum jump

# Time Complexity: O(n)
# Space Complexity: O(1)

"""
Observations:
1) We will always need to take at least one jump.

farthest: The maximum index we can reach at the moment.
lastPosition: Contains the maximum range seen after a jump has been made
Now, starting iteration from index 0, the above values are updated as follows:
    First we test whether we have reached the end of the array, in that case we just need to return the jump variable.
    Next we update the farthest. This is equal to the maximum of farthest and i+arr[i](the number of steps we can take from the current position).
    farthest = max(farthest,i+arr[i])
Since we know that it is possible somehow to reach farthest, we again initialize the lastPosition to the number of steps to reach farthest from position i.

"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        farthest = -1                  # farthest you can jump
        lastPosition = 0               # last position you should jump
        jumps = 0
        
        for i in range(len(nums)-1):
            farthest = max(nums[i]+ i, farthest)
            if i == lastPosition:
                jumps += 1
                lastPosition = farthest
    
        return jumps



# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def jump(self, ar):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(ar)
        minJumpIdx = 0
        res = [0 for i in range(n)]
        i = 1

        while(i < n and i > minJumpIdx):
            if minJumpIdx + ar[minJumpIdx] >= i:
                res[i] = res[minJumpIdx] + 1
                i += 1
            else:
                minJumpIdx += 1
                
        return res[-1]   