"""
computers = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]
n= 3

##################################################################
def dfs(computers, v):
    print(v, end=' ')

    for idx, node in enumerate(computers[v]):
        if idx == v:
            continue
        if not node == 0:
            computers[v][idx] = 0
            dfs(computers, idx)


# n은 노드 총 개수, computers는 2차원 배열 연결 여부
# 그니까 이거를 computers를 2차원 배열이자 동시에 visited로 사용해야해 그게 포인트인듯

def solution(n, computers):
    answer = 0
    # 방문기록을 주어진 2차원 배열을 이용할 것이다
    dfs(computers, 0)

    return answer


##################################################################

solution(n, computers)"""