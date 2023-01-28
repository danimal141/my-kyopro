from itertools import accumulate

h, w, n = map(int, input().split())
x = cs = [[0] * (w + 1) for _ in range(h + 1)]

for _ in range(n):
    a, b, c, d = map(int, input().split())

    x[a][b] += 1
    x[a][d + 1] -= 1
    x[c + 1][b] -= 1
    x[c + 1][d + 1] += 1

# w axis
cs = [list(accumulate(w_list)) for w_list in x]

# h axis
for j in range(1, w + 1):
    for i in range(1, h + 1):
        cs[i][j] = cs[i - 1][j] + cs[i][j]

for i in range(1, h + 1):
    out = " ".join(map(str, cs[i][1:]))
    print(out)
