"""
Problem Statement: Print Indentation Correctly

Given a string "(hello word (bye bye))"
Need to print:

(
    hello
  word
  (
    bye
    bye
  )
)

Language: Python
Written by: Mostofa Adib Shakib

References: 

=> https://leetcode.com/discuss/interview-question/409902/Snap-or-phone-or-print-indentation-correctly
"""

def printIndentationCorrectly(s):
  n = len(s)
  i=0
  count = 0

  while i < n:
      char = s[i]
      
      if char == ' ':
          i+=1
      elif char == '(':
          print(count * '    ' + char)
          count += 1
          i+=1
      elif char == ')':
          count -=1
          print(count * '    ' + char)
          i+=1
      else:
          j = i
          
          while j < n and s[j] != ' ' and s[j] != ')':
              j+=1
          print(count * '    ' + s[i:j])
          
          i = j

# Driver Code

testStringOne = "(hello word (bye bye))"
testStringTwo = '( (hi))'

printIndentationCorrectly(testStringOne)
printIndentationCorrectly(testStringTwo)