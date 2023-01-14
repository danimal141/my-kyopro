'''
> 5 40
> 10 20 30 40 50
=> [[5, 40], [10, 20, 30, 40, 50]]
'''
vals = [list(map(int,input().split())) for i in range(2)]

[_, x] = vals[0]
candidates = vals[1]

if x in candidates:
    print("Yes")
else:
    print("No")
