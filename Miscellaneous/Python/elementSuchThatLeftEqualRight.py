"""
Problem statement: Return the element such that the left hand side equals the right hand side

Written by: Mostofa Adib Shakib
Language: Python
"""

def elementSuchThatLeftEqualRight(arr):
  length = len(arr)
  prefixArray = [arr[0]] + [0] * (length-1)
  suffixArray = [0] * (length-1) + [arr[-1]]

  for i in range(1, length):
    prefixArray[i] =  prefixArray[i-1] + arr[i]
    suffixArray[length-1-i] = suffixArray[length-i] + arr[length-1-i]

  for i in range(length):
    if prefixArray[i] == suffixArray[i]:
      return arr[i]

arr = [ 2, 3, 4, 1, 4, 5]
print(elementSuchThatLeftEqualRight(arr))