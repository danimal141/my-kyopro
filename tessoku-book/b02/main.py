TARGET = 100
[a, b] = [int(val) for val in input().split()]

# Create the divisors list
matched = list(filter(lambda i: (TARGET % i) == 0, list(range(a, b)) + [b]))

if len(matched) > 0:
    print("Yes")
else:
    print("No")
