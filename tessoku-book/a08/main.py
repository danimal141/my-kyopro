from itertools import accumulate

h, w = map(int, input().split())
x = cs = [[0] * (w + 1)] * (h + 1)

for i in range(1, h + 1):
    x[i] = [0] + list(map(int, input().split()))

# h = w = 5
# x => [[0, 2, 0, 0, 5, 1], [0, 1, 0, 3, 0, 0], [0, 0, 8, 5, 0, 2], [0, 4, 1, 0, 0, 6], [0, 0, 9, 2, 7, 0]]
# cs (width) => [[0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 7, 8], [0, 1, 1, 4, 4, 4], [0, 0, 8, 13, 13, 15], [0, 4, 5, 5, 5, 11], [0, 0, 9, 11, 18, 18]]
# cs (height) => [[0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 7, 8], [0, 3, 3, 6, 11, 12], [0, 3, 11, 19, 24, 27], [0, 7, 16, 24, 29, 38], [0, 7, 25, 35, 47, 56]]

cs = [list(accumulate(w_list)) for w_list in x]

for j in range(1, w + 1):
    for i in range(1, h + 1):
        cs[i][j] = cs[i - 1][j] + cs[i][j]

q = int(input())

for _ in range(q):
    a, b, c, d = map(int, input().split())
    print(cs[c][d] + cs[a - 1][b - 1] - cs[a - 1][d] - cs[c][b - 1])
