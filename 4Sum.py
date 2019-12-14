"""
LeetCode Problem 18. 4Sum

Link: https://leetcode.com/problems/4sum/
Written by: Mostofa Adib Shakib
Language: Python

"""

# Solution 1 [Very efficient]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if nums == []:
            return []
        nums.sort()
        N = len(nums) 
        M = nums[-1]
        out = []
        dct = {j : i for i,j in enumerate(nums)}
        for i in range(N-3):
            a = nums[i]
            if 4 * a > target:
                break
            if a + 3*M < target:
                continue
            for j in range(i+1,N-2):                
                b = nums[j]
                if 3 * b + a > target:
                    break
                if a + b + 2 *M < target:
                    continue
                for k in range(j+1,N-1):
                    c = nums[k]
                    if a+b+2*c >target:
                        break
                    if a+b+c+M <target:
                        continue
                    d = target-a-b-c
                    if d in dct and dct[d] > k:
                        if [a,b,c,d] not in out:
                            out.append([a,b,c,d])
        return out


# Solution 2 [way less efficient]


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        length = len(nums) - 1
        
        if length < 3: return
        
        if length == 3:
            Sum = nums[0] + nums[1] + nums[2] + nums[3]
            if Sum == target:
                return [ [nums[0], nums[1], nums[2], nums[3]] ]
        
        nums = sorted(nums)
        
        result = []
        
        for i in range(length-2):
            for j in range(i+1, length-1):
                StartingIndex = j+1
                EndingIndex = length
                
                while StartingIndex < EndingIndex:
                    temp = []
                    Addition = nums[i] + nums[j] + nums[StartingIndex] + nums[EndingIndex]
                    
                    if Addition == target and i != j:
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[StartingIndex])
                        temp.append(nums[EndingIndex])
                        if temp not in result:
                            result.append(temp)
                        StartingIndex += 1
                        EndingIndex -= 1
                    
                    elif Addition > target:
                        EndingIndex -= 1
                    else:
                        StartingIndex += 1
                        
        return result

