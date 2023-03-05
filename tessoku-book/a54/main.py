q = int(input())
queries = [input().split() for _ in range(q)]

m = {}

for query in queries:
    if query[0] == "1":
        m[query[1]] = query[2]
    if query[0] == "2":
        print(m[query[1]])
