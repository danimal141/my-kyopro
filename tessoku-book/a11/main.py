n, x = map(int, input().split())
a = list(map(int, input().split()))

# from bisect import bisect_left
# We can also use `bisect.bisect_left`


# target_list should be sorted
def bin_search(val, target_list):
    left = 0
    right = len(target_list) - 1

    while right >= left:
        middle = (left + right) // 2

        if val > target_list[middle]:
            left = middle + 1
        elif val == target_list[middle]:
            return middle
        elif val < target_list[middle]:
            right = middle - 1


idx = bin_search(x, a)
print(idx + 1)
