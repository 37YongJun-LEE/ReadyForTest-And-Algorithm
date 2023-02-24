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




# visited 는 필수

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


# def bfs():
def bfs(graph, start, visited):
    visited[start] == True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        # 해당 노드와 연결된 노드들을 큐에 삽입한다.
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] == True

count = 0
for i in range(9):
    if not visited[i]:
        bfs(graph, 0, visited)
        count += 1 ## 개수를 세는 것이니 bfs 끝나면 개수 한개 증가,
                    ## 나머지 visited[]에


# def solution():














