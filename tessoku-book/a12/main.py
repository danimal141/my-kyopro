n, k = map(int, input().split())
a = list(map(int, input().split()))


def evaluate(sec, n, k, a):
    sum = 0
    for i in range(n):
        sum += sec // a[i]

    if sum >= k:
        return True
    else:
        return False


left_sec = 1
right_sec = 10**9

while left_sec < right_sec:
    mid_sec = (
        left_sec + right_sec
    ) // 2  # select seconds to evaluate like binary search
    ans = evaluate(mid_sec, n, k, a)

    if ans == False:  # noqa
        left_sec = mid_sec + 1
    elif ans == True:  # noqa
        right_sec = mid_sec

# After finishing the loop, left_sec would equal right_sec
print(left_sec)
