from collections import deque

"""
n = 9	
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
3

n = 4	
wires = [[1,2],[2,3],[3,4]]	
0

n =7	
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	
1
"""

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
from collections import deque

# 기존의 bfs함수에서 노드 개수 카운트 하는 것만 추가됨
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0

    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    # cnt 로 송전탑 개수 리턴 필요
    return cnt


def solution(n, wires):
    answer = n

    for i in range(n - 1):
        wires_copy = wires.copy()
        wires_copy.pop(i)
        graph = [[] for _ in range(n + 1)]

        for a, b in wires_copy:
            graph[a].append(b)
            graph[b].append(a)

        # 한쪽 그래프 안의 송전탑 개수는 어떻게 구할 것인가? 포인트
        # 그래프를 bfs방식으로 방문하며 개수를 세어본다.
        # 따라서 bfs 함수 생성 필요
        # 0부터 시작 안하고 1부터 시작하므로 n+1 필요
        visited = [False] * (n + 1)
        count = bfs(graph, 1, visited)    # 시작은 언제나 1부터 시작.
        answer = min(answer, abs((n - count) - count))
        # print(answer)
    return answer

solution(n, wires)