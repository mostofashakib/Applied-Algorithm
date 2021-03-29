"""
Pramp Problem: Word Count Engine
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

def word_count_engine(document):
  document = document.lower()
  document = document.strip()
  newString = ""
  
  for i in range(len(document)):
    if document[i] == " ":
      newString += " "
    elif document[i].isalpha():
      newString += document[i]
  
  documentArray = newString.split(" ")
  firstOccurance = {}
  hashMap = {}
  freqTable = {}
  length = len(documentArray)
  result = []
  
  for i in range(length):
    word = documentArray[i]
    
    if word == "":
      continue
    
    elif word not in hashMap:
      hashMap[word] = 1
      firstOccurance[word] = i
    else:
      hashMap[word] += 1
      
  for key, value in hashMap.items():
    if value not in freqTable:
      freqTable[value] = [(key, firstOccurance[key])]
    else:
      freqTable[value].append((key, firstOccurance[key]))
  
  for key, value in freqTable.items():
    if len(value) > 1:
      freqTable[key] = sorted(value, key = lambda x: x[1])
      
  sortedFreqTable = sorted(freqTable.items(), key = lambda x:x[0], reverse = True)
  
  for item in sortedFreqTable:
    count = item[0]
    temp = item[1]
    
    if len(temp) > 1:
      for i in range(len(temp)):
        result.append([temp[i][0], str(count)])
    else:
      result.append([temp[0][0], str(count)])
    
  return result