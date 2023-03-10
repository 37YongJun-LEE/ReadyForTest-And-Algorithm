import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

visited = [False]*(n)

graph = [ [] for _ in range(n) ]


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)
result = False


def dfs(v, depth):
    global result
    visited[v] = True
    if depth == 4:
        result = True
        return

    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[v] = False



for i in range(n):
    dfs(i, 0)
    if result:
        break

if result:
    print(1)
else:
    print(0)


