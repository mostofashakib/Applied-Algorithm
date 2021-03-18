"""
LeetCode Problem: 390. Elimination Game
Link: https://leetcode.com/problems/elimination-game/
Language: Python
Written by: Mostofa Adib Shakib
"""

# TIME COMPLEXITY : O(logN) #
# SPACE COMPLEXITY : O(1) #
# APPROACH : GREEDY

#      1 2 3 4 5 6 7 8 9 10 11 12 
# (r)   2 4 6 8 10 12 ( difference is 2, start is 2, level i.e i = 1, length i.e number of digits = 6 (even))
#      2 6 10        #1 ( diff = 4, n = 3(odd), start = 2)    (start is same as prev row)
# (r)   6             #2 ( from prev row, i = even, start will be removed any way)

#      1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
# (r)   2 4 6 8 10 12 14    ( difference is 2, start is 2, level i.e i = 1, length i.e number of digits = 7 (odd))
#      4 8 12           #3 ( start changed from prev row )
# (r)   8                #2 ( from prev row, i = even, start will be removed any way)

class Solution:
    def lastRemaining(self, n: int) -> int:

        iteration = 0 #record the iteration
        point = 1 #point to the first element in the list
        interval = 1 #record the interval between elements
        
        while(n>1):
            if n%2 == 1 or iteration%2==0:#if we eliminate from the left or the length of list is odd, the first element will move forward one place and the interval will double 
                point+=interval
                iteration+=1
                interval*=2
                n = n//2
            else: #if we eliminate the element from right and the length of list is even, the first element doesn't change
                iteration+=1
                interval*=2
                n = n//2
        return point


# Brute Force
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return n
        
        arr = [i for i in range(1, n+1)]
        flag = True
        
        while True:
            temp = []
            
            if flag:
                for i in range(1, len(arr), 2):
                    temp.append(arr[i])
                flag = False
                arr = temp
                
            else:
                arr = arr[::-1]
                for i in range(1, len(arr), 2):
                    temp.append(arr[i])
                flag = True
                arr = temp[::-1]
                
            if len(arr) == 1:
                return arr[0]