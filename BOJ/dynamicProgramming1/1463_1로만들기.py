# 바텀 업 방식 구현


# dp의 키 포인트는 메모리 공간을 상대적으로 좀 쓰더라도, 프로그램의 속도를 효율적으로 높이는 방식을 쓴다

# 별도로 메모리 공간을 할당하여 일련의 값들을 저장시키고, 다음 연산에 필요한 값들을 메모리에서 찾아서,
    # 이미 연산된 값은 새로 연산할 필요 없이 그저 호출로 가져다 사용하는 것이 커포인트이다.


# 주어진 문제 "1로 만들기"는 1이 될때까지의 연산을 전부 적용시켜 N이 1이 될때 까지 거치는 연산의 횟수만을 카운트하고 이를 메모리공간에 저장시킨다.
    # 이때 이전에 저장된 횟수와 새로 계산된 횟수 중에서, 최소값을 찾아 갱신하거나, 유지하는 방식을 사용한다.
n = int(input())


d = [0]*(n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[n])
