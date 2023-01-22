# sample
# 8
# 5
# 2 3
# 3 6
# 5 7
# 3 7
# 1 5

from itertools import accumulate

d = int(input())  # days
n = int(input())  # attendance number
diff_list = [0] * (d + 2)  # to trim the start and end

for _ in range(n):
    start, end = map(int, input().split())
    diff_list[start] += 1
    diff_list[end + 1] -= 1
cs = list(accumulate(diff_list))

for i in range(1, len(cs) - 1):
    print(cs[i])
