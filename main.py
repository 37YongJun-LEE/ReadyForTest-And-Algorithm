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



# DFS와 BFS 구현을 정확히 알아야한다.

# 주어진 그래프에서 연결된 노드를 깊이우선탐색으로 방문하는 법
def dfs(graph, v, visited):     # DFS는 스택을 이용한다.
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:              # if not 조건문: ==> 구조 설명: 조건문에 해당하지 않으면 실행하는 if문
            dfs(graph, i, visited)




visited = [False] * 9





