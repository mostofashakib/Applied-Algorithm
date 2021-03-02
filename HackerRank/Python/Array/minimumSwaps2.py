"""
Hacker Rank problem: Minimum Swaps 2
Link: https://www.hackerrank.com/challenges/minimum-swaps-2/problem
Written by: Mostofa Adib Shakib
Language: Python
"""

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ans = 0
    hashmap = {}
    sortedArray = sorted(arr)
    length = len(arr)
    
    for i in range(length):
        hashmap[arr[i]] = i
    
    for i in range(length):
        if arr[i] != sortedArray[i]:
            ans += 1
            
            temp = arr[i]
            
            arr[i], arr[hashmap[sortedArray[i]]]= arr[hashmap[sortedArray[i]]], arr[i]
            
            hashmap[temp] = hashmap[sortedArray[i]]
            hashmap[sortedArray[i]] = i
    
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()