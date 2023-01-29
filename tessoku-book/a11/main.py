n, x = map(int, input().split())
a = list(map(int, input().split()))

# n = 15
# x = 47
# a = 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67

# ans = 11 (index: 10)

target_range = range(0, n)
idx = n // 2  # // means rounding division

while len(target_range) > 1:
    first_range = target_range[:idx]
    second_range = target_range[idx:]

    target_range = first_range if x in [a[i] for i in first_range] else second_range

    idx = int(len(target_range) / 2)

print(target_range[0] + 1)
