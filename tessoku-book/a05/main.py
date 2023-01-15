n, k = map(int, input().split())
matched_count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        expected = k - (i + j)
        if expected >= 1 and expected <= n:
            matched_count += 1

print(matched_count)
