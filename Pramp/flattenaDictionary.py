"""
Pramp Problem: Getting a Different Number
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

# Solution 2

def flatten_dictionary(dictionary):
  hashMap = {}

  def recursiveHelper(preKey, value):
    for key, val in value.items():
      
      if key == "":
          hashMap[preKey] = val

      elif type(val) != dict:
        if preKey == "":
          hashMap[key] = val
        else:
          hashMap[preKey + "." + key] = val
      else:
        if preKey == "":
          recursiveHelper(key, val)
        else:
          recursiveHelper(preKey + "." + key, val)
  
  for key, value in dictionary.items():
    if type(value) != dict:
      hashMap[key] = value
    else:
      recursiveHelper(key, value)
      
  return hashMap