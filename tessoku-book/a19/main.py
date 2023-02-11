"""
n, w = 4 7

w, v
3 13
3 17
5 29
1 10

w = [0, 3, 3, 5, 1]
v = [0, 13, 17, 29, 10]
"""

n, w = map(int, input().split())
weights = [0] * (n + 1)
values = [0] * (n + 1)

for i in range(1, n + 1):
    weights[i], values[i] = map(int, input().split())

# dynamic programming
# assign -1 to avoid select untarget values when checking max
dp = [[-1] * (w + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(0, w + 1):
        if j < weights[i]:
            dp[i][j] = dp[i - 1][j]
        elif j >= weights[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])
print(max(dp[n]))
