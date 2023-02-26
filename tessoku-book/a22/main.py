n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [-(10**9)] * (n + 1)
dp[1] = 0

# dynamic programming
for i in range(1, n):
    dp[a[i - 1]] = max(dp[a[i - 1]], dp[i] + 100)
    dp[b[i - 1]] = max(dp[b[i - 1]], dp[i] + 150)

print(dp[n])
