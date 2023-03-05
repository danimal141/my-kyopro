import heapq

q = int(input())
queries = [input().split() for _ in range(q)]

t = []

for query in queries:
    if query[0] == "1":
        heapq.heappush(t, int(query[1]))
    if query[0] == "2":
        print(t[0])
    if query[0] == "3":
        heapq.heappop(t)
