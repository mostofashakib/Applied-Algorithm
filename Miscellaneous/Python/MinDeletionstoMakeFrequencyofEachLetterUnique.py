"""
Problem Statement: Min Deletions to Make Frequency of Each Letter Unique

Minimum number of characters to delete from a string so that each character appears unique number of times.

Note: You can delete all occurances of characters.

eg: "aaaabbbb" -> 1 "a" or 1"b" would make "a" and "b" appear unique number of times.

Language: Python
Written by: Mostofa Adib Shakib

References: 

=> https://medium.com/@molchevsky/best-solutions-for-microsoft-interview-tasks-min-deletions-to-make-frequency-of-each-letter-unique-16adb3ec694e
=> https://stackoverflow.com/questions/57933350/find-the-minimum-number-of-deletions-to-get-a-unique-count-of-every-alphabet
=> https://iq.opengenus.org/minimum-deletion-for-unique-frequency/
"""

from collections import Counter

def find_answer(s):
  if len(s)  == 0:
    return 0

  cnts = list(Counter(s).values())
  cnts.sort(reverse=True)
  deletes = 0
  for i in range(1, len(cnts)):
      while cnts[i] >= cnts[i-1] and cnts[i] > 0: # only delete while count > 0
        cnts[i] -= 1
        deletes += 1

  return deletes

print(find_answer("opengenus"))   #6
print(find_answer("ccaaffddecee"))  #6
print(find_answer('abcabc')) #3
print(find_answer('aaabbcc')) #1
print(find_answer('aaabbbccc')) #3
print(find_answer('aaabbbcccddd')) #6