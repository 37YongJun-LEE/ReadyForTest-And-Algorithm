import sys
n = int(input())

graph = []

for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

## 아이디어 다시 생각
        # 2차원 배열에서 한 좌표와 인접한 다른 4가지 방향의 좌표들을 -- > 그럴 필요가 없다 결국 바꾼것이 아래행과 겹치게 되므로
        # 탐색후 같은 것이 있으면 바꾸기, 없으면 다른 탐색 방향 이동        -> 오른쪽과 밑에것만 바꿔주면 가능
        # 바꾼다음, 행과 열을 기준으로 4가지색 전면 재탐색 가장 길이가 긴 부분리턴

        # check 함수를 만들어서 전체 탐색 해주기


def check(graph):
    answer = 1
    n = len(graph)
    for i in range(n):
        cnt = 1
        # 행 검사
        for j in range(1, n):
            if graph[i][j] == graph[j][j-1]:
                cnt += 1
            else:
                cnt = 1
        if answer < cnt:
            answer = cnt

        # 열 검사
        cnt = 1
        for j in range(1, n):
            if graph[j][i] == graph[j-1][i]:
                cnt += 1
            else:
                cnt = 1
        if answer < cnt:
            answer = cnt

    return answer



# check 함수 만들었으니 이제 바꾸고 나서 check 쓰기
answer = 0

for i in range(n):
    for j in range(n):


        # 현재 위치와 왼쪽 바꾸기
        if j+1 < n:     # 넘어가지 않게 조정
            graph[i][j] , graph[i][j+1] = graph[i][j+1], graph[i][j] # 양옆 바꾸기
            result1 = check(graph)
            if result1 > answer:
                answer = result1

            graph[i][j] , graph[i][j+1] = graph[i][j+1], graph[i][j] # 원래대로 돌려놓기


        # 현재 위치와 밑 바꾸기
        if i+1 < n:
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j] # 아래 위 바꾸기
            result2 = check(graph)
            if result2 > answer:
                answer = result2

            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j] # 원래대로 돌려놓기


print(answer)




"""
import sys
input=sys.stdin.readline

def check(arr):
    n=len(arr)
    answer=1

    for i in range(n):
        # 열 순회하면서 연속되는 숫자 세기
        cnt=1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
        	# 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
            # 이전과 다르다면 다시 1로 초기화
                cnt=1
                
            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

        # 행 순회하면서 연속되는 숫자 세기
        cnt=1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
        	# 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
            # 이전과 다르다면 다시 1로 초기화
                cnt=1
                
            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

    return answer

n=int(input())
arr=[list(input()) for _ in range(n)]
answer=0

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n:
        	# 인점한 것과 바꾸기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            
            # check는 arrd에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp=check(arr)

            if temp > answer:
                answer = temp
               
            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        # 행 바꾸기
        if i+1 < n:
        	# 인점한 것과 바꾸기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
            # check는 arrd에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp=check(arr)

            if temp > answer:
                answer = temp
            
            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
print(answer)
"""