"""
Link: 
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(1)
"""

T = int(input())

for x in range(1, T + 1):
    N, M, Q = map(int, input().split())
    
    min1 = (M-Q) + (N-Q+1) + (M-1)
    min2 = (M-1) + 1 + N
    
    y = min(min1, min2)
    
    print("Case #{}: {}".format(x, y), flush = True)