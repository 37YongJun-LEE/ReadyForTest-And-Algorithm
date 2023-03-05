import sys
n = int(input())

graph = []

for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

## 아이디어 다시 생각
        # 2차원 배열에서 한 좌표와 인접한 다른 4가지 방향의 좌표들을
        # 탐색후 같은 것이 있으면 바꾸기, 없으면 다른 탐색 방향 이동
        # 바꾼다음, 행과 열을 기준으로 4가지색 전면 재탐색 가장 길이가 긴 부분리턴
        