# array
# a0, a1, a2, ...an-1

# cumulative sum array
# s0, s1, s2, ...sn-1, sn
# s0 = a0
# s1 = a0 + a1
# s2 = a0 + a1 + a2

from itertools import accumulate

n, q = map(int, input().split())
a = list(map(int, input().split()))
# cs = [sum(a[:i+1]) for i in range(len(a))]

# Maybe, I can use numpy.cumsum instead.
# https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html
cs = [0] + list(accumulate(a))

for _ in range(q):
    l, r = map(int, input().split())
    result = cs[r] - cs[l - 1]
    print(result)
