import sys
sys.setrecursionlimit(200000)

# DFS 구현하기
def dfs(start):
    visited[start] = True
    #print(start, end=' ')

    for k in graph[start]:
        if not visited[k]:
            return dfs(k)


n = int(input())        # 총 그래프 개수 입력
for i in range(n):
    V, E = map(int, sys.stdin.readline().split())   # 각 그래프당 추어지는 노드와 간선 개수 입력
    graph = [ [] for i in range(V+1) ]
    visited = [False]*(V+1)
    
    for j in range(1, E+1):     # 그래프 각 노드당 연결된 정보 입력
        node1, node2 = map(int, sys.stdin.readline().split())
        graph[node1].append(node2)
        graph[node2].append(node1)      # 그래프 그리기 완료

    #확인코드
    #print(graph)
    #print(visited)


    # 입력받은 그래프로 YES, NO 판별하기
    if V > E:
        dfs(1)
        visited.pop(0)
        if False not in visited:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')














