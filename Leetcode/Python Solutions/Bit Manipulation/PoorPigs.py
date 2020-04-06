"""
LeetCode Problem: 458. Poor Pigs
Link: https://leetcode.com/problems/poor-pigs/
Language: Python
Written by: Mostofa Adib Shakib

Intuition:

How many states does a pig have:
    If there is no time to test, i.e. minutesToTest / minutesToDie = 0, the pig has only one state - alive.
    If minutesToTest / minutesToDie = 1 then the pig has a time to die from the poison, that means that now there are two states available for the pig : alive or dead.
    One more step. If minutesToTest / minutesToDie = 2 then there are three available states for the pig : alive / dead after the first test / dead after the second test.

The number of available states for the pig is states = minutesToTest / minutesToDie + 1.

How many buckets could test x pigs with 2 available states:       (Think about combination)
    One pig could test 2 buckets - let's make him drink from the bucket number 1 and then wait minutesToDie time.
    If he is alive - the poison is in the bucket number 2.
    If he is dead - the poison is in the bucket number 1.
    The same way two pigs could test 2^2 = 4 
    Hence if one pig has two available states, x pigs could test 2^x

How many buckets could test x pigs with s available states:  s^x

Algorithm:

Find x such that pigs = log(buckets)/log(states) (lower bound)
"""



class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = (minutesToTest//minutesToDie) +1
        return math.ceil(math.log(buckets)/math.log(states))