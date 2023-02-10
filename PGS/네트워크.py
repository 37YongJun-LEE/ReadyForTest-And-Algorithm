from collections import deque

def bfs(computers, start, visited):
    queue = deque([start])
    visited[start] = 1
    return_graph = []

    while queue:
        v = queue.popleft()
        # print(v, end=' ')
        return_graph.append(v)
        for idx, num in enumerate(computers[v]):
            if num != 0 and visited[idx] != 1:
                queue.append(idx)
                visited[idx] = 1
    return_graph.sort()

    return return_graph


def solution(n, computers):
    answer = 0
    answer_set = []

    for i in range(n):
        visited = [0] * n  # 방문 = 1 , 미방분 = 0
        bfs_return = bfs(computers, i, visited)
        if bfs_return not in answer_set:
            answer_set.append(bfs_return)

    return len(answer_set)
