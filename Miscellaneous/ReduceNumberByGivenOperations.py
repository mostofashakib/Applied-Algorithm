"""
Problem Statement: Reduce a number to 1 by performing given operations


Given number in binary form, if its even -> you can divide it by 2; if its odd -> you can substract 1 from it.
You can repeat above steps as many times as you want to reach 0. How many steps it took to reach zero?

Language: Python
Written by: Mostofa Adib Shakib

References: https://www.geeksforgeeks.org/reduce-a-number-to-1-by-performing-given-operations/

Reduce a given number N to 1 in the minimum number of steps

Operations you can perform:
      1) If the number is even then you can divide the number by 2
      2) If the number is odd then you are allowed to perform either (n+1) or (n-1)
"""

def countways(n): 
    if n == 1: 
        return 0 
    elif n % 2 == 0: 
        return 1 + countways(n / 2)
    else: 
        return 1 + min(countways(n - 1), countways(n + 1))
  
# Driver code 
n = 15; 
print(countways(n))