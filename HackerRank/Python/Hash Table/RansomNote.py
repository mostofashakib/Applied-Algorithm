"""
Hacker Rank problem: Hash Tables: Ransom Note
Link: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
Written by: Mostofa Adib Shakib
Language: Python
"""

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below

def checkMagazine(magazine, note):
    n = len(note)
    count = 0
    hashmap = {}

    for i in note:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    for i in magazine:
        if i in hashmap and hashmap[i] > 0:
            hashmap[i] -= 1
            count += 1

    if count == n:
        print("Yes")
    else:
        print("No")

# Boilerplate code

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
