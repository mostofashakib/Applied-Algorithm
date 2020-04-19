"""
Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(1)
"""

T = int(input())

for x in range(1, T + 1):
    N = int(input())
    Q = [int(s) for s in input().split(" ")]
    
    y = 0

    for i in range(1, len(Q)-1):
        if Q[i] > Q[i-1] and Q[i+1] < Q[i]:
            y += 1
    
    print("Case #{}: {}".format(x, y), flush = True)