from collections import deque

q = int(input())
queries = [input().split() for _ in range(q)]

s = deque()

for query in queries:
    if query[0] == "1":
        s.append(query[1])
    if query[0] == "2":
        print(s[0])
    if query[0] == "3":
        s.popleft()
