n = int(input())
a = [0] + list(map(int, input().split()))
d = int(input())

for _ in range(1, d + 1):
    l, r = map(int, input().split())
    print(max(max(a[:l]), max(a[r:])))
