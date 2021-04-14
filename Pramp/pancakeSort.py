"""
Pramp Problem: Pancake Sort
Language: Python
Written by: Mostofa Adib Shakib
"""

def pancake_sort(arr):
  
  if len(arr) == 1:
    return arr
      
  def flip(arr, k):
    first = 0
    last = k
    
    while first < last:
      arr[first], arr[last] = arr[last], arr[first]
      first += 1
      last -= 1
  
  k = len(arr) - 1
  
  while k > 0:
    maximumValue = float('-inf')
    maximumIndex = 0
    
    for j in range(k+1):
      if arr[j] > maximumValue:
        maximumValue = arr[j]
        maximumIndex = j
    
    if maximumIndex != 0:
      flip(arr, maximumIndex)
      
    flip(arr, k)
    k-= 1
    
  return arr