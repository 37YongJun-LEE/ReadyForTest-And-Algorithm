
# BFS는 큐를 이용한다. from collections import deque
                    # queue = deque()

# BFS는 DFS와 반대로 현재 노드에서 최대한 가까이 있는 노드들을 우선으로 방문하는 방식

# DFS와는 다르게 실제로 deque()를 활용해 구현하여야한다. 

# BFS 동작방식
    # 탐색 시작 노드를 큐에 삽입하고, 방문처리한다.
        # 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
            # 2번 과정을 재귀적으로 반복하지 못할 때 까지 수행


# BFS 정의
from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])          # queue에 start 삽입
    visited[start] = True           # start 노드 (현재노드) 방문처리

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 노드와 연결된, 아직 방문하지 않은 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



visited = [False] * 9       # 보면 알겠지만, visited는 현재 False가 9개인 방문기록 리스트이다.

graph = [               # 그래프는 노드가 1이 가장 작으므로 인덱스까지 맞추기위해서 0에 빈배열 삽입
    [],             #
    [2,3,8],        # 1
    [1,7],          # 2
    [1,4,5],        # 3
    [3,5],          # 4
    [3,4],          # 5
    [7],            # 6
    [2,6,8],        # 7
    [1,7]           # 8
]

bfs(graph, 1, visited)


# from collections import deque
def bfs2(graph2, start2, visited2):
    # 먼저 bfs 구현의 근간이 되는 queue 생성
    queue = deque([start2])        # 처음 시작 노드 start2 큐 생성과 동시에 큐 삽입
    visited2[start2] = True     # 처음 시작 노드 start2 방문처리

    # 방문하지 않은 start2와 연결된 노드들 queue가 빌 때까지 방문하기
    while queue:
        v = queue.popleft()     # v는 큐에서 빠진 방금 방문처리한 노드
        print(v, end=' ')

        # 연결된 노드중에서 방문처리가 안된 노드가 있으면 큐에 넣고 방문처리하기
        for i in graph2[v]:
            if not visited2[i]:     # 해당 노드 i 방문처리 안되어있으면
                queue.append(i)
                visited2[i] = True

visited2 = [False] * 9       # 보면 알겠지만, visited는 현재 False가 9개인 방문기록 리스트이다.

graph2 = [               # 그래프는 노드가 1이 가장 작으므로 인덱스까지 맞추기위해서 0에 빈배열 삽입
    [],             #
    [2,3,8],        # 1
    [1,7],          # 2
    [1,4,5],        # 3
    [3,5],          # 4
    [3,4],          # 5
    [7],            # 6
    [2,6,8],        # 7
    [1,7]           # 8
]
print()
print('----------------------------')
bfs2(graph2, 1, visited2)
