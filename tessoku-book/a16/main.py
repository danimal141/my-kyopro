n = int(input())
a = [0] * 2 + list(map(int, input().split()))
b = [0] * 3 + list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = 0  # It takes 0 min to move to the room1 from the room1
dp[2] = a[2]

for i in range(3, n + 1):
    dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i])

print(dp[n])
