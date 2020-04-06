
# Time complexity: O(n*m)
# Space Complexity: O(n)

tc = int(input().strip())
for t in range(tc):
    n, k, p = map(int, input().strip().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split())))
        for j in range(1, k):
            arr[i][j] = arr[i][j] + arr[i][j-1]
    
    
    memo = []
    memo = [[-1] * (p + 1) for i in range(n + 1)]

    def dp(n, p, k):
        if memo[n][p] != -1:
            return memo[n][p]
        
        if p > (n * k) or n <= 0 or p <= 0:
            ans = 0
        else:
            ans = dp(n - 1, p, k)
            lim = min([k, p])
            for i in range(1, lim + 1):
                tmp = arr[n - 1][i - 1] + dp(n - 1, p - i, k)
                ans = max([ans, tmp])    
        memo[n][p] = ans
        return ans

    ans = dp(n, p, k)
    print('Case #' + str(t + 1) + ': ' + str(ans))
        