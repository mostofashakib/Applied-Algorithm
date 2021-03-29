"""
Pramp Problem: Getting a Different Number
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

def get_different_number(arr):
  smallestInteger = 0
  arr = sorted(arr)
  
  for elem in arr:
    if elem == smallestInteger:
      smallestInteger += 1
    else:
      return smallestInteger
  
  return smallestInteger