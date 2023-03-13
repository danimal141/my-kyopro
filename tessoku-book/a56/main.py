n, q = map(int, input().split())
s = input()
queries = [list(map(int, input().split())) for i in range(q)]

# ord(c) gets the ASCII code of the string
# https://docs.python.org/3/library/functions.html?highlight=ord#ord
t = list(map(lambda c: ord(c) - ord("a") + 1, s))

MOD = 2147483647
power100 = [None] * (n + 1)
power100[0] = 1
for i in range(n):
    power100[i + 1] = power100[i] * 100 % MOD

h = [None] * (n + 1)
h[0] = 0
for i in range(n):
    h[i + 1] = (h[i] * 100 + t[i]) % MOD


def hash_value(left, right):
    return (h[right] - h[left - 1] * power100[right - left + 1]) % MOD


for a, b, c, d in queries:
    hash1 = hash_value(a, b)
    hash2 = hash_value(c, d)
    if hash1 == hash2:
        print("Yes")
    else:
        print("No")
