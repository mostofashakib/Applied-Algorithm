"""
Problem Statement: Minimum Number of Platforms Required for a Railway/Bus Station
Language: Python
Written by: Mostofa Adib Shakib
Reference: https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

Time Complexity: O(n)
Space Complexity: O(1)
"""

def findPlatform(arrival, departure, n):
  arrival.sort()
  departure.sort()
  i = 1
  j = 0
  platformNeeded = 1
  maxPlatform = 1


  while i < n and j < n:
    if arrival[i] <= departure[j]:
      i += 1
      platformNeeded += 1

    else:
      j += 1
      platformNeeded -= 1

    maxPlatform = max(maxPlatform, platformNeeded)

  return maxPlatform

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

print("Minimum Number of Platforms Required = ", findPlatform(arr, dep, n))