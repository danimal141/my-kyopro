TARGET_NUM = 100
[a, b] = [int(val) for val in input().split()]

matched = list(filter(lambda i: (TARGET_NUM / i).is_integer(), range(a, b)))

if len(matched) > 0:
    print("Yes")
else:
    print("No")
