"""
LeetCode Problem 670. Maximum Swap
Link: https://leetcode.com/problems/maximum-swap/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        numString = str(num)
        numArray = list(numString)
        sortedNumArray = sorted(numArray, reverse = True)
        length = len(numArray)
        startingIndex = 0
        maximum = num
        maxNum = float('-inf')
        maxNumIdx = 0
        
        if sortedNumArray == numArray:
            return num
        
        for i in range(length):
            if sortedNumArray[i] == numArray[i]:
                startingIndex += 1
            else:
                break
        
        for i in range(length-1, startingIndex, -1):
            number = int(numArray[i])
            if number > maxNum:
                maxNum = number
                maxNumIdx = i
                
        numArray[startingIndex], numArray[maxNumIdx] = numArray[maxNumIdx], numArray[startingIndex]
        val = int(''.join(numArray))
        maximum = max(maximum, val)
        
        return maximum