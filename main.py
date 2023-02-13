# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print ("Hello world")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#################################################################
""" 이곳은 연습장 입니다. """
#################################################################



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


# dfs의 기본이 뭐라고? 스택과 재귀함수


# bfs의 기본은 뭐? 큐가 전부다

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(graph, 1, visited)



