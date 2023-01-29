n = int(input())
a = list(map(int, input().split()))
d = int(input())

# TLE
# for _ in range(1, d + 1):
#     l, r = map(int, input().split())
#     print(max(max(a[:l]), max(a[r:])))
#
# ------------
#
# a = [1, 2, 5, 5, 2, 3, 1]
# p = [1, 2, 5, 5, 5, 5, 5]
# q = [5, 5, 5, 5, 3, 3, 1]

# l, r = 3, 5 => 2, 4
# p[l - 1] = 2
# q[r + 1] = 3

# l, r = 4, 6 => 3, 5
# p[l - 1] = 5
# q[r + 1] = 1

p = [0] * n
q = [0] * n

# initialize
p[0] = a[0]

for i in range(1, n):
    p[i] = max(p[i - 1], a[i])

# initialize
q[n - 1] = a[n - 1]

for i in reversed(range(0, n - 1)):
    q[i] = max(q[i + 1], a[i])

for _ in range(d):
    l, r = map(int, input().split())
    # convert to a list index
    l -= 1
    r -= 1
    print(max(p[l - 1], q[r + 1]))
