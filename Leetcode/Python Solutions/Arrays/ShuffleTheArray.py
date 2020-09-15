""" 
LeetCode Problem: 1470. Shuffle the Array
Link: https://leetcode.com/problems/shuffle-the-array/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""
Constant space solution
Time Complexity: O(n^2)
Space complexity: O(1)
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        count = n-1
        firstPointer = n-1
        secondPointer = n
        
        while count > 0:
            loops = count
            pointer_one = firstPointer
            pointer_two = secondPointer
            
            while loops > 0:
                nums[pointer_one], nums[pointer_two] = nums[pointer_two], nums[pointer_one]
                pointer_one -= 1
                pointer_two -= 1
                loops -= 1
            count -= 1
            firstPointer += 1
            secondPointer += 1
            
        return nums

"""
Linear time solution
Time Complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        
        for i in range(0, n):
            result.append(nums[i])
            result.append(nums[n+i])
            
        return result


