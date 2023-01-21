from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))
q = int(input())

cs_win = [0] + list(accumulate(a))
cs_lose = [i - j for i, j in zip(range(len(a) + 1), cs_win)]

for _ in range(q):
    l, r = map(int, input().split())
    win_result = cs_win[r] - cs_win[l - 1]
    lose_result = cs_lose[r] - cs_lose[l - 1]

    if win_result > lose_result:
        print("win")
    elif win_result == lose_result:
        print("draw")
    else:
        print("lose")
