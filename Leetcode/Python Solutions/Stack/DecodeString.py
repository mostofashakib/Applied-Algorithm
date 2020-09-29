"""
LeetCode Problem: 394. Decode String
Link: https://leetcode.com/problems/decode-string/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Time complexity: O(maxK⋅n)
# Space complexity: O(2n)

# Two Stacks Approach

class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        charStack = []
        n = len(s)
        i = 0
        
        while i < n:
            if s[i].isdigit():
                count = 0                
                while s[i].isdigit():
                    count = count * 10 + int(s[i])
                    i = i+1
                numStack.append(count)
                
            elif s[i] == "]":
                substring = ""
                while charStack[-1] != "[":
                    substring = charStack.pop() + substring
                charStack.pop()
                temp = numStack.pop() * substring
                charStack.append(temp)
                i += 1
            else:
                charStack.append(s[i])
                i += 1
                
        return "".join(charStack)


# One Stack Approach
# Time complexity: O(maxK⋅n)
# Space complexity: O(n)

"""
Iterate through the string, and push everything to a stack until you've found a right bracket. Once you've found a right bracket,
you use that and pop from the stack to evaluate the innermost expression in the string. For example, if you have 2[a3[b]], your stack would
be [2, "[", "a", 3, "[", "b"] when it reaches the first right bracket. Once it reaches the first right bracket, it attempts to evaluate everything
in the innermost bracket by popping from the stack to form the entire string you need to multiply, and finding the number you need to multiply by. 
After this, the stack will look like: [2, "[", "a", "bbb" ]. The innermost expression of 3, "[", "b" was turned into bbb and put back into the stack.
At the next right bracket, we will similarily evaluate the innermost bracket, so that the stack turns into ["abbbabbb"]. If there are multiple sets of
enclosed brackets in the expression, our stack will end up with multiple strings in the end. Simply join them for the result.
"""

class Solution:
    def decodeString(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                current = ''
                while stack:
                    val = stack.pop()
                    if val ==  "[":
                        break
                    current = val + current
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*current)
            else:
                stack.append(s[i])
        return ''.join(stack)