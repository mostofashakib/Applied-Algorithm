"""
LeetCode Problem: 4. Median of Two Sorted Arrays
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution:
    def fullJustify(self, words, maxWidth):
        answer = []
        length = len(words)
                
        for i in range(1, length):
            res = ""
            total = 0
            
            if self.isEven(words) == True and i <= length -3:
                total = maxWidth - len(words[i-1]) - len(words[i])
                res += words[i-1] + " " * total + words[i]
                answer.append(res)

            if self.isEven(words) == False and i <= length -2:
                total = maxWidth - len(words[i-1]) - len(words[i])
                res += words[i-1] + " " * total + words[i]
                answer.append(res)

            elif self.isEven(words) == True and i > length-3:
                total = maxWidth - len(words[i-1]) - len(words[i]) -1
                res += words[i-1] + " " + words[i] + " " * total
                answer.append(res)

            elif self.isEven(words) == False and i > length-2:
                total = maxWidth - len(words[i-1]) - len(words[i]) -1
                res += words[i-1] + " " + words[i] + " " * total
                answer.append(res)

        return answer

    
    def isEven(self, array):
        length = len(array)
        
        if length % 2 == 0:
            return True
        else:
            return False

ob = Solution()
print(ob.fullJustify(["This", "is", "an", "example", "of", "text", "justification"], 16))

