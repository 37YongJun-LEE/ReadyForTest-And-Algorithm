import sys
sys.setrecursionlimit(10**6)

# 테스트 케이스의 개수
t = int(sys.stdin.readline())

# 현재 노드와 이웃한 노드 탐색
def dfs(node):

    global result

    for neighbor in graph[node]:

        # 이웃 노드에 색칠이 되어있지 않다면
        if (visited[neighbor] == -1):

            # 현재 노드가 1로 색칠되어있다면
            if (visited[node] == 1):
                visited[neighbor] = 2
            # 현재 노드가 2로 색칠되어있다면
            if (visited[node] == 2):
                visited[neighbor] = 1

            dfs(neighbor)

        # 이웃 노드에 색칠이 되어있다면
        else:

            # 현재 노드와 동일한 색깔이라면
            if (visited[node] == visited[neighbor]):

                result = False
                return

for _ in range(t):

    # 정점의 개수 V와 간선의 개수 E
    v, e = map(int, sys.stdin.readline().split())

    # 색칠 여부 저장
    visited = [-1] * (v+1)

    # 양방향 간선 정보 저장
    graph = [[] for _ in range(v+1)]

    # 양방향 간선 정보 저장
    for _ in range(e):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)

    # 이분 그래프 여부
    result = True

    # 모든 노드 탐색
    for i in range(1, v+1):

        # 현재 노드가 색칠 되어있지 않다면
        if (visited[i] == -1):

            # 현재 노드를 색칠
            visited[i] = 1

            # 이웃한 노드에 대해서 색칠
            dfs(i)

            # 현재 노드로부터 이분 그래프가 아닌것을 확인했다면
            if (result == False):
                break

    # 이분 그래프가 아니라면
    if (result == False):
        print("NO")
    # 이분 그래프라면
    else:
        print("YES")