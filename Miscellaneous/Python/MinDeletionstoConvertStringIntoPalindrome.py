"""
Problem Statement: Find the minimum number of deletions required to convert a string into palindrome
Language: Python
Written by: Mostofa Adib Shakib

Reference: https://www.techiedelight.com/find-minimum-number-deletions-convert-string-into-palindrome/
"""

def minDeletions(X, i, j):

  # base condition
  if i >= j:
    return 0

  # if last character of the is same as the first character
  if X[i] == X[j]:
    return minDeletions(X, i + 1, j - 1)

  # else if last character of is different to the first character

  # 1. Remove last character & recur for the remaining substring
  # 2. Remove first character & recur for the remaining substring

  # return 1 (for remove operation) + minimum of the two values

  return 1 + min(minDeletions(X, i, j - 1), minDeletions(X, i + 1, j))


if __name__ == '__main__':

  X = "ACBCDBAA"
  n = len(X)

  print("The minimum number of deletions required are", minDeletions(X, 0, n - 1))
