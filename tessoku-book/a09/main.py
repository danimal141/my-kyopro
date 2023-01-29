from itertools import accumulate

h, w, n = map(int, input().split())
x = [[0] * (w + 2) for _ in range(h + 2)]
cs = [[0] * (w + 2) for _ in range(h + 2)]

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
    # fmt: off
    out = " ".join(map(str, cs[i][1:w + 1]))  # noqa
    # fmt: on
    print(out)
