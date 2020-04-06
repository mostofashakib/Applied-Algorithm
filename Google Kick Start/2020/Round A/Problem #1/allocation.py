T = int(input())

for x in range(1, T + 1):
    N, P = map(int, input().split())
    S = map(int, input().split())
    S = sorted(S)
    MinHouses = 0

    for i in S:
        if P >= 0 and i <= P:
            P -= i
            MinHouses += 1
    
    print("Case #{}: {}".format(x, MinHouses), flush = True)