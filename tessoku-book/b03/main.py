import sys

TARGET_SUM = 1000
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if a[i] + a[j] + a[k] == TARGET_SUM:
                print("Yes")
                sys.exit()
print("No")
