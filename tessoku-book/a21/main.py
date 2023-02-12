n = int(input())

p = [0] * (n + 1)
a = [0] * (n + 1)

for i in range(1, n + 1):
    p[i], a[i] = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][n] = 0

# len indicates right - left
for len in reversed(range(0, n - 1)):
    for left in range(1, n - len + 1):
        right = left + len

        # when removing the l - 1 block
        score1 = 0
        if left >= 2 and p[left - 1] >= left and p[left - 1] <= right:
            score1 = a[left - 1]

        # when removing the r + 1 block
        score2 = 0
        if right <= n - 1 and p[right + 1] >= left and p[right + 1] <= right:
            score2 = a[right + 1]

        if left == 1:
            dp[left][right] = dp[left][right + 1] + score2
        elif right == n:
            dp[left][right] = dp[left - 1][right] + score1
        else:
            dp[left][right] = max(
                dp[left - 1][right] + score1, dp[left][right + 1] + score2
            )

ans = 0
for i in range(1, n + 1):
    ans = max(ans, dp[i][i])

print(ans)
