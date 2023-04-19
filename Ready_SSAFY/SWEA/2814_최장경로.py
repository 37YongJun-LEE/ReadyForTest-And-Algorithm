def dfs(graph, v, visited, depth):
    global langth
    visited[v] = True
    #print(v, depth)
    langth = max(langth, depth)
    #print(depth)
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited, depth+1)
            visited[i] = False          ### 이부분 중요... 어렵다 dfs

    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    if M == 0:
        print('#{} {}'.format(test_case, 1))
        continue

    #print(N, M)
    graph = [[] for _ in range(N+1)]

    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    #print(graph)
    # dfs() 시작은 1부터 0 부터 하면 에러남
    # for 문으로 정점 1부터 N 까지 돌면서 cnt 를 갱신한다.
    langth = 0

    for i in range(1, N+1):
        visited = [False] * (N + 1)

        dfs(graph, i, visited, 1)
        #print(i, langth)

    print('#{} {}'.format(test_case, langth))



"""
다 맞게 작성하셨는데 위의 코드에서 딱 한 줄 실수하신 부분이 있습니다.
재귀함수를 호출하시면서 처음에 진입할 때 v 정점을 True로 하시고 시작을 하게 되는데,
해당정점에서 더 이상 갈 수 없어서 이 전 정점으로 돌아왔을 경우 False를 해주셔야 다른 정점을 통해서 끝까지 도달할 수 있습니다.
 
즉, 위의 코드에서
dfs(graph, i, visited, depth+1) 아래에
visited[i] = False 를 넣어주시면 정상적으로 Pass 되는 것을 확인하실 수 있습니다.

"""

"""
1
3 2
1 2
3 2
"""



"""
1
6 5
1 2
1 3
2 4
2 5
2 6

"""

"""
1
6 4
1 3
2 4
2 5
2 6

"""


"""
1
6 3
1 3
2 5
2 6

"""