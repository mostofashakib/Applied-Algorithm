"""
Pramp Problem: Pairs with Specific Difference
Language: Python
Written by: Mostofa Adib Shakib
"""

# Solution: 1
# Time Complexity: O(N)
# Space Complexity: O(N)

def find_pairs_with_given_difference(arr, k):
  hashMap = {}
  length = len(arr)
  result = []
  
  if length == 0:
    return result
  
  for num in arr:
    hashMap[num-k] = num
    
  for num in arr:
    if num in hashMap:
      result.append([hashMap[num], num])
      
  return result

# Solution: 2
# Time Complexity: O(NlogN)
# Space Complexity: O(N)

def find_pairs_with_given_difference(arr, k):
  lastOccurance = {}
  length = len(arr)
  
  # Key, Index pair for the occurance of Y
  for idx in range(length):
    number = arr[idx]
    
    if number not in lastOccurance:
      lastOccurance[number] = idx
  
  temp = []
  
  for idx in range(length):
    numberX = arr[idx]
    
    numberY = numberX - k
    
    if numberY in lastOccurance:
      numberYIndex = lastOccurance[numberY]      
      temp.append((numberX, numberY, numberYIndex))
  
  temp = sorted(temp, key = lambda x: x[2])
  result = []
  
  for X, Y, idx in temp:
    result.append([X, Y])
      
  return result