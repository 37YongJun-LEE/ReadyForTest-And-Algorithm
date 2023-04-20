def dfs(index, cnt, num_sum):
    global result
    # 먼저 합 계산을 해주고 나서 ,다음 인덱스인 경우에 추가하지 않고 넘겨주는 방식으로 작성해야한다.
    # 그래야 해당 인덱스을때 계산이 안되서 건너뛰어지는 경우가 발생하지 않는다.
    if cnt == 3:    # cnt 가 4인경우에 3개의 합이 저장되어있다.
        result.append(num_sum)
    if index == 7:
        return
    num = data[index]
    # 선택한경우
    dfs(index+1, cnt+1, num_sum+num)
    # 선택안한경우
    dfs(index+1, cnt, num_sum)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    result = []
    # dfs(index, cnt, num_sum)
    dfs(0, 0, 0)
    result = list(set(result))
    result.sort()
    print('#{} {}'.format(test_case, result[-5]))


"""

2
1 2 3 4 5 6 7
5 24 99 76 1 77 6

"""
