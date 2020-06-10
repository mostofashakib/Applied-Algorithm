"""
Printing the Longest Common Subsequence
Written by: Mostofa Adib Shakib
Language: Python
"""

def printLongestCommonSubsequence(text1, text2):
    n = len(text1) # row
    m = len(text2) # column
    
    # initializing dp table
    
    dp = [ [0 for i in range(m+1)] for j in range(n+1) ]
    
    # building up the dp table
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # getting the size of the LCS string
    
    index = dp[-1][-1]
    charArray = [""] * index
    i = n
    j = m
    
    while i > 0 and j > 0:
        # if the characters in both the strings are a match then move diagonally to the left
        if text1[i-1] == text2[j-1]:
            charArray[index-1] = text1[i-1]
            index -= 1
            i -= 1
            j -= 1
        
        # if the characters in both the strings are not a match then move to the left or right
        # depending on whichever cell has the higher value
        
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1   # moves up
        else:
            j -= 1   # moves to the left
            
    LongestCommonSubsequenceString = ''.join(charArray)
    
    return LongestCommonSubsequenceString

print(printLongestCommonSubsequence("abcde", "ace"))

    
